"""
Sample script showing how to use Syllabus-GPT programmatically
without the Streamlit UI.

This is useful for:
- Batch processing
- Integration with other tools
- Automated testing
- Custom interfaces
"""

import os
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import FAISS
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory
from langchain.schema import Document


def process_pdfs(pdf_paths):
    """
    Process PDF files and create a vector store.
    
    Args:
        pdf_paths (list): List of paths to PDF files
        
    Returns:
        FAISS: Vector store with processed documents
    """
    documents = []
    
    # Extract text with metadata
    for pdf_path in pdf_paths:
        with open(pdf_path, 'rb') as file:
            pdf_reader = PdfReader(file)
            filename = os.path.basename(pdf_path)
            
            for page_num, page in enumerate(pdf_reader.pages):
                text = page.extract_text()
                if text.strip():
                    doc = Document(
                        page_content=text,
                        metadata={
                            "source": filename,
                            "page": page_num + 1
                        }
                    )
                    documents.append(doc)
    
    print(f"Extracted {len(documents)} pages")
    
    # Split into chunks
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len,
        separators=["\n\n", "\n", " ", ""]
    )
    chunks = text_splitter.split_documents(documents)
    print(f"Created {len(chunks)} chunks")
    
    # Create vector store
    embeddings = OpenAIEmbeddings()
    vectorstore = FAISS.from_documents(documents=chunks, embedding=embeddings)
    print("Vector store created")
    
    return vectorstore


def create_qa_chain(vectorstore):
    """
    Create a QA chain with the vector store.
    
    Args:
        vectorstore: FAISS vector store
        
    Returns:
        ConversationalRetrievalChain: QA chain
    """
    llm = ChatOpenAI(temperature=0.3, model_name="gpt-3.5-turbo")
    
    memory = ConversationBufferMemory(
        memory_key='chat_history',
        return_messages=True,
        output_key='answer'
    )
    
    qa_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=vectorstore.as_retriever(search_kwargs={"k": 3}),
        memory=memory,
        return_source_documents=True
    )
    
    return qa_chain


def format_sources(source_documents):
    """Format source documents into readable citations."""
    if not source_documents:
        return "No sources found"
    
    sources_dict = {}
    for doc in source_documents:
        source = doc.metadata.get('source', 'Unknown')
        page = doc.metadata.get('page', 'Unknown')
        
        if source not in sources_dict:
            sources_dict[source] = set()
        sources_dict[source].add(page)
    
    citations = []
    for source, pages in sources_dict.items():
        sorted_pages = sorted(list(pages))
        page_str = ", ".join([f"p. {p}" for p in sorted_pages])
        citations.append(f"{source} ({page_str})")
    
    return " | ".join(citations)


def ask_question(qa_chain, question):
    """
    Ask a question and get an answer with sources.
    
    Args:
        qa_chain: Conversational retrieval chain
        question (str): Question to ask
        
    Returns:
        dict: Answer and sources
    """
    response = qa_chain({'question': question})
    
    answer = response.get('answer', 'No answer generated')
    source_docs = response.get('source_documents', [])
    sources = format_sources(source_docs)
    
    return {
        'answer': answer,
        'sources': sources
    }


def main():
    """Main function demonstrating programmatic usage."""
    
    # Load environment variables
    load_dotenv()
    
    # Check for API key
    if not os.getenv('OPENAI_API_KEY'):
        print("Error: OPENAI_API_KEY not found in environment")
        return
    
    # Example: Process PDFs
    print("=" * 50)
    print("Processing PDFs...")
    print("=" * 50)
    
    # Replace with your PDF paths
    pdf_paths = [
        "path/to/your/syllabus1.pdf",
        "path/to/your/syllabus2.pdf",
    ]
    
    try:
        vectorstore = process_pdfs(pdf_paths)
        qa_chain = create_qa_chain(vectorstore)
        
        print("\n" + "=" * 50)
        print("Ready for questions!")
        print("=" * 50)
        
        # Example questions
        questions = [
            "What is the grading breakdown?",
            "When is the final exam?",
            "What are the course prerequisites?",
        ]
        
        for question in questions:
            print(f"\nQ: {question}")
            result = ask_question(qa_chain, question)
            print(f"A: {result['answer']}")
            print(f"Sources: {result['sources']}")
            print("-" * 50)
        
        # Interactive mode
        print("\n" + "=" * 50)
        print("Interactive mode (type 'quit' to exit)")
        print("=" * 50)
        
        while True:
            question = input("\nYour question: ").strip()
            
            if question.lower() in ['quit', 'exit', 'q']:
                break
            
            if not question:
                continue
            
            result = ask_question(qa_chain, question)
            print(f"\nAnswer: {result['answer']}")
            print(f"Sources: {result['sources']}")
    
    except FileNotFoundError as e:
        print(f"Error: Could not find PDF file - {e}")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
