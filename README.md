# 🎓 Syllabus-GPT

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.29.0-red.svg)](https://streamlit.io/)
[![LangChain](https://img.shields.io/badge/LangChain-0.1.0-green.svg)](https://python.langchain.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**Your intelligent course assistant that answers questions about your syllabi, lecture notes, and course materials with source citations.**

## 🌟 Features

- **📚 Multi-Document Support**: Upload multiple course PDFs (syllabi, slides, notes) simultaneously
- **🔍 Source Citations**: Every answer includes specific document names and page numbers
- **💬 Conversational Interface**: Natural language Q&A with context retention
- **🎯 Academic-Focused**: Optimized specifically for university course materials
- **⚡ Fast & Efficient**: Uses FAISS for rapid similarity search
- **🎨 Beautiful UI**: Clean, modern interface with academic theme

## 🚀 What Makes This Different?

Unlike generic PDF chatbots, **Syllabus-GPT** is specifically designed for students and educators:

1. **Source Attribution**: Automatically cites which document and page each answer comes from
2. **Course-Optimized**: Understands academic structures like grading policies, assignment deadlines, and course schedules
3. **Batch Processing**: Handle entire semesters worth of materials at once
4. **Professional UI**: Academic-themed interface perfect for educational settings

## 📸 Demo

> 📝 **Screenshot Coming Soon!** Run the app locally to see it in action. See [DEMO_SCREENSHOT.md](DEMO_SCREENSHOT.md) for instructions.

**What You'll See:**
- Clean, academic-themed interface
- Natural language question input
- AI-powered answers with **automatic source citations**
- Example: *"What is the grading breakdown?" → Answer with citation: "📄 CS301_AI_Syllabus.pdf (p. 1)"*

Try it yourself with the sample syllabus in `examples/sample_syllabi/`!

## 🛠️ Installation

### Prerequisites

- Python 3.8 or higher
- OpenAI API key ([Get one here](https://platform.openai.com/api-keys))

### Setup Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/AIdoAI/syllabus-gpt.git
   cd syllabus-gpt
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   
   Create a `.env` file in the project root:
   ```bash
   OPENAI_API_KEY=your_api_key_here
   ```

## 🎯 Usage

1. **Start the application**
   ```bash
   streamlit run app.py
   ```

2. **Upload your course materials**
   - Click "Browse files" in the sidebar
   - Select your PDFs (syllabi, lecture slides, notes, etc.)
   - Click "🔄 Process Documents"

3. **Ask questions!**
   - "What's the grading breakdown for this course?"
   - "When is the final exam?"
   - "What are the prerequisites?"
   - "What topics are covered in week 5?"

4. **Review source citations**
   - Every answer includes citations showing the exact document and page numbers
   - Use these to verify information or dive deeper into the material

## 🏗️ Architecture

```
┌─────────────────┐
│   PDF Upload    │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Text Extraction │ ← PyPDF2
│  with Metadata  │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Text Chunking  │ ← RecursiveCharacterTextSplitter
│  (with sources) │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│   Embeddings    │ ← OpenAI Embeddings
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Vector Storage  │ ← FAISS
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Question Asked  │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Similarity      │
│ Search (top 3)  │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ LLM Processing  │ ← ChatGPT
│ with Context    │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Answer + Sources│
└─────────────────┘
```

## 💡 Technical Highlights

### Key Improvements Over Base Code

1. **Document Metadata Preservation**
   ```python
   # Old: Lost source information
   text += page.extract_text()
   
   # New: Preserves document name and page number
   doc = Document(
       page_content=text,
       metadata={"source": pdf.name, "page": page_num + 1}
   )
   ```

2. **Enhanced Text Splitting**
   ```python
   # Old: Simple character splitter
   CharacterTextSplitter(separator="\n", chunk_size=1000)
   
   # New: Recursive splitter with better boundaries
   RecursiveCharacterTextSplitter(
       chunk_size=1000,
       chunk_overlap=200,
       separators=["\n\n", "\n", " ", ""]
   )
   ```

3. **Source Citation System**
   ```python
   def format_sources(source_documents):
       """Groups citations by document and lists unique pages"""
       # Returns: "📄 syllabus.pdf (p. 3, p. 7)"
   ```

4. **Return Source Documents**
   ```python
   ConversationalRetrievalChain.from_llm(
       return_source_documents=True  # Critical for citations
   )
   ```

## 🎓 Use Cases

- **Students**: Quickly find information across multiple course syllabi
- **TAs**: Answer common student questions efficiently
- **Professors**: Review and summarize course materials
- **Advisors**: Help students understand course requirements
- **Study Groups**: Collaborative exploration of course content

## 🔧 Customization

### Changing the LLM Model

Edit `app.py`:
```python
llm = ChatOpenAI(
    temperature=0.3,
    model_name="gpt-4"  # Use GPT-4 for better answers
)
```

### Adjusting Retrieved Documents

```python
retriever=vectorstore.as_retriever(
    search_kwargs={"k": 5}  # Retrieve 5 instead of 3 chunks
)
```

### Customizing Chunk Size

```python
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1500,  # Larger chunks
    chunk_overlap=300,  # More overlap
)
```

## 📁 Project Structure

```
syllabus-gpt/
├── app.py                 # Main application
├── htmlTemplates.py       # UI styling
├── requirements.txt       # Dependencies
├── .env.example          # Environment template
├── .gitignore            # Git ignore rules
├── README.md             # This file
└── demo.png              # Screenshot
```

## 🤝 Contributing

This is a portfolio/resume project, but suggestions and improvements are welcome!

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 🐛 Known Issues & Future Enhancements

- [ ] Add support for non-English course materials
- [ ] Implement export chat history feature
- [ ] Add support for other document formats (DOCX, PPTX)
- [ ] Create summary view of all uploaded documents
- [ ] Add ability to highlight text in original PDFs
- [ ] Implement user authentication for multi-user support

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Built with [LangChain](https://python.langchain.com/)
- UI powered by [Streamlit](https://streamlit.io/)
- Embeddings by [OpenAI](https://openai.com/)
- Vector storage by [FAISS](https://github.com/facebookresearch/faiss)

## 📬 Contact

**Ziyi Ai**
- 📧 Email: ziyi.ai.cn@gmail.com
- 💼 LinkedIn: [linkedin.com/in/ziyi-a-90b29a17a](https://www.linkedin.com/in/ziyi-a-90b29a17a)
- 🐙 GitHub: [github.com/AIdoAI](https://github.com/AIdoAI)

Project Link: [https://github.com/AIdoAI/syllabus-gpt](https://github.com/AIdoAI/syllabus-gpt)

---

⭐ If you find this project helpful, please give it a star!
