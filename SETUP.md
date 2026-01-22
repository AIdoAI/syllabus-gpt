# 🚀 Syllabus-GPT Setup Guide

This guide will walk you through setting up Syllabus-GPT on your local machine.

## Prerequisites

Before you begin, ensure you have:

- Python 3.8 or higher installed
- pip (Python package manager)
- An OpenAI API key
- Git (for cloning the repository)

## Step-by-Step Installation

### 1. Clone the Repository

```bash
git clone https://github.com/AIdoAI/syllabus-gpt.git
cd syllabus-gpt
```

### 2. Create a Virtual Environment (Recommended)

**On macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

**On Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

You should see `(venv)` at the beginning of your terminal prompt.

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

This will install:
- `streamlit` - Web interface
- `langchain` - LLM orchestration
- `openai` - OpenAI API client
- `PyPDF2` - PDF processing
- `faiss-cpu` - Vector similarity search
- `python-dotenv` - Environment variable management

### 4. Get Your OpenAI API Key

1. Go to [OpenAI's platform](https://platform.openai.com/)
2. Sign in or create an account
3. Navigate to API keys
4. Click "Create new secret key"
5. Copy the key (you won't see it again!)

### 5. Configure Environment Variables

Create a `.env` file in the project root:

```bash
cp .env.example .env
```

Edit `.env` and add your API key:

```
OPENAI_API_KEY=sk-proj-xxxxxxxxxxxxx
```

**Important:** Never commit your `.env` file to GitHub!

### 6. Run the Application

```bash
streamlit run app.py
```

The app should automatically open in your browser at `http://localhost:8501`

## First-Time Usage

1. **Upload Course PDFs**
   - Click the "Browse files" button in the sidebar
   - Select one or more PDF files (syllabi, lecture notes, etc.)
   - Wait for files to upload

2. **Process Documents**
   - Click the "🔄 Process Documents" button
   - Wait for processing to complete (you'll see progress messages)
   - Once done, you're ready to ask questions!

3. **Ask Questions**
   - Type your question in the text input
   - Press Enter
   - View the answer with source citations

## Troubleshooting

### Common Issues

#### "No module named 'streamlit'"
**Solution:** Make sure you've activated your virtual environment and installed requirements:
```bash
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
```

#### "OpenAI API key not found"
**Solution:** Check that:
1. You created a `.env` file (not `.env.txt`)
2. The file contains `OPENAI_API_KEY=your_key_here`
3. There are no spaces around the `=` sign
4. The file is in the same directory as `app.py`

#### "Rate limit exceeded"
**Solution:** You've exceeded OpenAI's rate limits. Wait a few minutes and try again, or upgrade your OpenAI plan.

#### "PDF extraction failed"
**Solution:** Some PDFs are scanned images. Use PDFs with selectable text. You can use OCR tools to convert scanned PDFs first.

#### Port already in use
**Solution:** If port 8501 is busy:
```bash
streamlit run app.py --server.port 8502
```

## Testing Your Installation

Here's a quick test to ensure everything works:

1. Download a sample syllabus PDF
2. Upload it to Syllabus-GPT
3. Click "Process Documents"
4. Ask: "What topics are covered in this course?"
5. Verify you get an answer with source citations

## Performance Tips

### Speed Up Processing
- Use PDFs with clear, extractable text
- Smaller PDFs process faster
- Process multiple PDFs at once instead of one at a time

### Reduce Costs
- Use `gpt-3.5-turbo` (default) instead of `gpt-4`
- Ask focused questions
- Don't reload the same documents repeatedly

### Improve Accuracy
- Upload complete, well-formatted syllabi
- Include all relevant course materials
- Ask specific, clear questions

## Updating the Application

To get the latest version:

```bash
git pull origin main
pip install -r requirements.txt --upgrade
```

## Uninstallation

To remove Syllabus-GPT:

1. Deactivate the virtual environment:
   ```bash
   deactivate
   ```

2. Delete the project folder:
   ```bash
   cd ..
   rm -rf syllabus-gpt
   ```

## Next Steps

- Read the [README.md](README.md) for feature details
- Check out the [Architecture section](README.md#architecture) to understand how it works
- Customize the UI in `htmlTemplates.py`
- Modify chunking parameters in `app.py`

## Getting Help

If you encounter issues:

1. Check the [Troubleshooting](#troubleshooting) section above
2. Review OpenAI's [API documentation](https://platform.openai.com/docs)
3. Check LangChain's [documentation](https://python.langchain.com/)
4. Open an issue on [GitHub](https://github.com/AIdoAI/syllabus-gpt/issues)

---

Happy learning! 🎓
