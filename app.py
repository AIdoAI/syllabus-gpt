import streamlit as st
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import FAISS
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from htmlTemplates import css, bot_template, user_template
from langchain.schema import Document
import os


def get_pdf_text_with_metadata(pdf_docs):
    """
    Extract text from PDFs while preserving metadata about source and page numbers.
    Returns a list of Document objects with content and metadata.
    """
    documents = []
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        for page_num, page in enumerate(pdf_reader.pages):
            text = page.extract_text()
            if text.strip():  # Only add non-empty pages
                doc = Document(
                    page_content=text,
                    metadata={
                        "source": pdf.name,
                        "page": page_num + 1  # 1-indexed for user display
                    }
                )
                documents.append(doc)
    return documents


def get_text_chunks_with_metadata(documents):
    """
    Split documents into chunks while preserving metadata.
    Uses RecursiveCharacterTextSplitter for better chunking.
    """
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len,
        separators=["\n\n", "\n", " ", ""]
    )
    chunks = text_splitter.split_documents(documents)
    return chunks


def get_vectorstore(text_chunks):
    """
    Create a FAISS vector store from text chunks with metadata.
    """
    embeddings = OpenAIEmbeddings()
    vectorstore = FAISS.from_documents(documents=text_chunks, embedding=embeddings)
    return vectorstore


def get_conversation_chain(vectorstore):
    """
    Create a conversational retrieval chain with source documents.
    """
    llm = ChatOpenAI(temperature=0.3, model_name="gpt-3.5-turbo")
    
    memory = ConversationBufferMemory(
        memory_key='chat_history', 
        return_messages=True,
        output_key='answer'
    )
    
    conversation_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=vectorstore.as_retriever(search_kwargs={"k": 3}),
        memory=memory,
        return_source_documents=True,
        verbose=True
    )
    return conversation_chain


def format_sources(source_documents):
    """
    Format source documents into a readable citation string.
    Groups citations by document and lists unique pages.
    """
    if not source_documents:
        return ""
    
    # Group by source document
    sources_dict = {}
    for doc in source_documents:
        source = doc.metadata.get('source', 'Unknown')
        page = doc.metadata.get('page', 'Unknown')
        
        if source not in sources_dict:
            sources_dict[source] = set()
        sources_dict[source].add(page)
    
    # Format citations
    citations = []
    for source, pages in sources_dict.items():
        sorted_pages = sorted(list(pages))
        page_str = ", ".join([f"p. {p}" for p in sorted_pages])
        citations.append(f"📄 **{source}** ({page_str})")
    
    return "\n".join(citations)


def handle_userinput(user_question):
    """
    Handle user input and display response with source citations.
    """
    try:
        response = st.session_state.conversation({'question': user_question})
        st.session_state.chat_history = response['chat_history']
        
        # Get the answer and source documents
        answer = response.get('answer', '')
        source_documents = response.get('source_documents', [])
        
        # Format sources
        sources = format_sources(source_documents)
        
        # Display conversation
        for i, message in enumerate(st.session_state.chat_history):
            if i % 2 == 0:
                st.write(user_template.replace(
                    "{{MSG}}", message.content), unsafe_allow_html=True)
            else:
                # For bot messages, append sources if this is the latest message
                if i == len(st.session_state.chat_history) - 1 and sources:
                    full_response = f"{message.content}\n\n---\n**Sources:**\n{sources}"
                else:
                    full_response = message.content
                st.write(bot_template.replace(
                    "{{MSG}}", full_response), unsafe_allow_html=True)
    
    except Exception as e:
        st.error(f"Error processing your question: {str(e)}")


def main():
    load_dotenv()
    
    st.set_page_config(
        page_title="Syllabus-GPT: Your Course Assistant",
        page_icon="🎓",
        layout="wide"
    )
    st.write(css, unsafe_allow_html=True)

    # Initialize session state
    if "conversation" not in st.session_state:
        st.session_state.conversation = None
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = None
    if "processed_files" not in st.session_state:
        st.session_state.processed_files = []

    # Header
    st.title("🎓 Syllabus-GPT")
    st.markdown("*Your intelligent course syllabus and materials assistant*")
    st.markdown("---")

    # Main chat interface
    user_question = st.text_input(
        "Ask me anything about your course materials:",
        placeholder="e.g., What are the grading policies? When is the midterm?"
    )
    
    if user_question:
        if st.session_state.conversation is None:
            st.warning("⚠️ Please upload and process your course PDFs first!")
        else:
            handle_userinput(user_question)

    # Sidebar
    with st.sidebar:
        st.header("📚 Course Documents")
        st.markdown("Upload your syllabi, lecture notes, and course materials")
        
        pdf_docs = st.file_uploader(
            "Upload PDFs (syllabi, slides, notes, etc.)",
            accept_multiple_files=True,
            type=['pdf']
        )
        
        if st.button("🔄 Process Documents", type="primary"):
            if not pdf_docs:
                st.error("Please upload at least one PDF file!")
            else:
                with st.spinner("Processing your course materials..."):
                    try:
                        # Extract text with metadata
                        documents = get_pdf_text_with_metadata(pdf_docs)
                        st.success(f"✅ Extracted text from {len(documents)} pages")

                        # Create text chunks with metadata
                        text_chunks = get_text_chunks_with_metadata(documents)
                        st.success(f"✅ Created {len(text_chunks)} searchable chunks")

                        # Create vector store
                        vectorstore = get_vectorstore(text_chunks)
                        st.success("✅ Built knowledge base")

                        # Create conversation chain
                        st.session_state.conversation = get_conversation_chain(vectorstore)
                        st.session_state.processed_files = [pdf.name for pdf in pdf_docs]
                        st.success("✅ Ready to answer your questions!")
                        
                    except Exception as e:
                        st.error(f"Error processing documents: {str(e)}")
        
        # Display processed files
        if st.session_state.processed_files:
            st.markdown("---")
            st.subheader("📋 Loaded Documents")
            for filename in st.session_state.processed_files:
                st.markdown(f"✓ {filename}")
        
        # Info section
        st.markdown("---")
        st.markdown("### 💡 Tips")
        st.markdown("""
        - Upload all your course syllabi at once
        - Include lecture slides and notes for better answers
        - Ask specific questions for more accurate results
        - All answers include source citations!
        """)
        
        # About section
        st.markdown("---")
        st.markdown("### ℹ️ About")
        st.markdown("""
        **Syllabus-GPT** uses AI to help you quickly find information 
        in your course materials. Every answer includes citations 
        showing exactly which document and page the information came from.
        """)


if __name__ == '__main__':
    main()
