# ⚡ Quick Start Guide

Get Syllabus-GPT running in 5 minutes!

## Prerequisites
- Python 3.8+
- OpenAI API key

## Installation (Copy & Paste)

```bash
# Clone the repo
git clone https://github.com/AIdoAI/syllabus-gpt.git
cd syllabus-gpt

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Create .env file
echo "OPENAI_API_KEY=your_key_here" > .env
```

## Configuration

Edit `.env` and replace `your_key_here` with your actual OpenAI API key.

## Run

```bash
streamlit run app.py
```

## First Use

1. Upload your course PDFs in the sidebar
2. Click "🔄 Process Documents"
3. Ask questions!

**Example Questions:**
- "What are the grading policies?"
- "When is the midterm exam?"
- "What are the required textbooks?"

## Common Issues

**"Module not found"**: Activate venv first
```bash
source venv/bin/activate
```

**"API key not found"**: Check your `.env` file exists and has the correct format

**"PDF won't upload"**: Ensure it's a text-based PDF (not a scanned image)

## Next Steps

- See [SETUP.md](SETUP.md) for detailed installation
- Read [README.md](README.md) for full documentation
- Check [CHANGELOG.md](CHANGELOG.md) for improvements made

---

Need help? Open an issue on GitHub!
