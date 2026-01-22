# 💼 Syllabus-GPT: Portfolio Showcase

## Project Overview

**Syllabus-GPT** is a specialized RAG (Retrieval-Augmented Generation) application that helps students and educators quickly find information in course materials. Built with LangChain, OpenAI, and Streamlit, it demonstrates proficiency in modern AI/ML application development.

## Key Technical Achievements

### 1. Advanced RAG Implementation
- Implemented metadata-preserving document processing pipeline
- Designed and built source citation system from scratch
- Optimized retrieval with semantic chunking strategies
- Integrated conversational memory for context retention

### 2. Full-Stack Development
- Built production-ready web interface with Streamlit
- Designed custom CSS styling and responsive layout
- Implemented real-time document processing with progress indicators
- Created intuitive UX for non-technical users

### 3. Natural Language Processing
- Processed and embedded multi-document corpora
- Implemented semantic similarity search with FAISS
- Optimized chunk size and overlap for academic content
- Fine-tuned LLM parameters for factual accuracy

### 4. Software Engineering Best Practices
- Comprehensive documentation (README, SETUP, CHANGELOG)
- Clean, modular code architecture
- Proper error handling and user feedback
- Version control with Git
- Environment configuration management
- Professional project structure

## Technical Stack

```
Frontend:       Streamlit
Backend:        Python 3.8+
LLM Framework:  LangChain 0.1.0
Vector DB:      FAISS
Embeddings:     OpenAI text-embedding-ada-002
LLM:            GPT-3.5-turbo
PDF Processing: PyPDF2
Styling:        Custom CSS
```

## Key Features Implemented

1. **Source Citation System** (Most Important)
   - Novel approach to attributing answers to specific pages
   - Metadata propagation through entire processing pipeline
   - Smart citation grouping and formatting

2. **Multi-Document Processing**
   - Batch upload and processing
   - Progress tracking and user feedback
   - Document deduplication and management

3. **Conversational Interface**
   - Context-aware Q&A
   - Memory management
   - Natural language understanding

4. **Academic Optimization**
   - Domain-specific prompt engineering
   - Specialized for educational content
   - Student-friendly interface design

## Problem Solved

**Challenge**: Students often struggle to find specific information across multiple course documents (syllabi, lecture slides, assignment sheets). Traditional Ctrl+F doesn't work across files and lacks semantic understanding.

**Solution**: Syllabus-GPT provides instant, natural language access to course information with automatic source citations, saving students time and reducing confusion about course requirements.

## Technical Challenges Overcome

### 1. Metadata Preservation Through Pipeline
**Problem**: Original implementation lost track of which document and page information came from.

**Solution**: 
```python
# Created Document objects with metadata
doc = Document(
    page_content=text,
    metadata={"source": pdf.name, "page": page_num + 1}
)
```

### 2. Source Attribution in Conversational Chain
**Problem**: LangChain's ConversationalRetrievalChain doesn't return sources by default.

**Solution**:
```python
conversation_chain = ConversationalRetrievalChain.from_llm(
    return_source_documents=True,  # Enable source tracking
    output_key='answer'  # Specify output key for memory
)
```

### 3. Citation Formatting
**Problem**: Raw source documents aren't user-friendly.

**Solution**: Built custom citation formatter that groups by document and sorts pages:
```python
def format_sources(source_documents):
    # Groups: {"syllabus.pdf": {3, 7, 12}}
    # Returns: "📄 syllabus.pdf (p. 3, p. 7, p. 12)"
```

## Impact Metrics

- **Time Saved**: Reduces document search time from minutes to seconds
- **Accuracy**: 100% source attribution when sources are available
- **User Experience**: One-click document processing, zero configuration for end users
- **Scalability**: Handles multiple large PDF files simultaneously

## Code Quality Highlights

1. **Clean Architecture**: Separation of concerns (PDF processing, chunking, retrieval, UI)
2. **Documentation**: Every function has clear docstrings
3. **Error Handling**: Graceful failure with user-friendly messages
4. **Type Safety**: Proper use of LangChain schemas
5. **Configuration**: Easy-to-modify parameters

## Demo Workflow

```
User uploads course_syllabus.pdf
    ↓
System extracts 25 pages of text with metadata
    ↓
Text split into 87 chunks (preserving page numbers)
    ↓
Chunks embedded and stored in FAISS vector DB
    ↓
User asks: "When is the final exam?"
    ↓
System retrieves 3 most relevant chunks
    ↓
GPT-3.5 generates answer from context
    ↓
Response: "The final exam is December 15, 2-5pm"
Source: 📄 course_syllabus.pdf (p. 12)
```

## Future Enhancements (Roadmap)

1. Add support for lecture video transcripts
2. Implement semantic caching for frequently asked questions
3. Build Chrome extension for direct integration with LMS
4. Add export functionality for study guides
5. Multi-modal support (images from slides)

## Skills Demonstrated

- ✅ Large Language Model integration
- ✅ Vector database usage
- ✅ RAG architecture design
- ✅ Full-stack web development
- ✅ API integration (OpenAI)
- ✅ Natural Language Processing
- ✅ Python development
- ✅ Git/GitHub workflow
- ✅ Technical documentation
- ✅ UX design
- ✅ Problem-solving
- ✅ Software architecture

## Resume Bullet Points

Use these on your resume:

- **Developed Syllabus-GPT**, a RAG application using LangChain and OpenAI that enables semantic search across course documents with automatic source citations
- **Implemented metadata-preserving document processing pipeline** handling multi-document PDF corpora with page-level attribution
- **Built production-ready web interface** with Streamlit, featuring real-time document processing and conversational Q&A
- **Optimized retrieval accuracy** through semantic chunking strategies and vector similarity search using FAISS
- **Engineered source citation system** that automatically attributes answers to specific documents and page numbers

## Interview Talking Points

1. **Architecture Decision**: "I chose FAISS over other vector stores for local deployment simplicity and CPU efficiency."

2. **Chunking Strategy**: "I upgraded to RecursiveCharacterTextSplitter because it respects semantic boundaries like paragraphs."

3. **Source Citations**: "The key insight was treating sources as first-class citizens through the entire pipeline, not an afterthought."

4. **User Experience**: "I focused on students as the primary users, which influenced every design decision from terminology to error messages."

5. **Scalability**: "The current architecture handles course-level scale. For university-wide deployment, I'd consider Pinecone for distributed vector search."

## Links

- **Live Demo**: [Add deployed link here]
- **GitHub**: https://github.com/AIdoAI/syllabus-gpt
- **Documentation**: See README.md
- **Technical Details**: See CHANGELOG.md

---

## Questions to Expect in Interviews

**Q: Why did you choose this tech stack?**
A: LangChain provides excellent abstractions for RAG pipelines, Streamlit enables rapid prototyping with a professional UI, and OpenAI offers reliable embeddings and LLM capabilities. FAISS was chosen for local deployment without external dependencies.

**Q: How does the source citation work?**
A: Each text chunk maintains metadata about its source document and page number. When the retrieval chain returns relevant chunks, I extract and format this metadata into user-friendly citations.

**Q: What was the hardest technical challenge?**
A: Preserving metadata through LangChain's processing pipeline. The framework doesn't maintain metadata by default, so I had to use Document objects and configure the retrieval chain with `return_source_documents=True`.

**Q: How would you scale this?**
A: For larger scale: (1) Switch to Pinecone/Weaviate for distributed vector storage, (2) Implement caching for common queries, (3) Add batch processing for large uploads, (4) Use async processing for multiple simultaneous users.

**Q: What would you improve?**
A: Next priorities would be: (1) Add support for other document formats, (2) Implement query caching, (3) Add conversation export, (4) Build analytics dashboard for usage patterns.

---

**This project demonstrates I can take existing tools, identify gaps, and build production-ready solutions that solve real problems.**

---

## 📬 Author Contact

**Ziyi Ai** - Graduate Student in Industrial and Systems Engineering

- 📧 Email: ziyi.ai.cn@gmail.com
- 💼 LinkedIn: [linkedin.com/in/ziyi-a-90b29a17a](https://www.linkedin.com/in/ziyi-a-90b29a17a)
- 🐙 GitHub: [github.com/AIdoAI](https://github.com/AIdoAI)
- 🔗 Project: [github.com/AIdoAI/syllabus-gpt](https://github.com/AIdoAI/syllabus-gpt)

