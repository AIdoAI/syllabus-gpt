# 🔧 Troubleshooting Common Errors

## Error: "Client.init() got an unexpected keyword argument 'proxies'"

### What This Means
This is a **version compatibility issue** between `langchain`, `langchain-community`, `langchain-openai`, and `openai` packages.

### ✅ Solution: Use Updated Requirements

**If you're getting this error**, you're using the old `requirements.txt`. The project has been updated with compatible versions.

### Quick Fix

**Option 1: Re-download the Project**
1. Download the latest `syllabus-gpt.zip`
2. Extract it
3. Use the new `requirements.txt`

**Option 2: Manual Update**

Update your `requirements.txt` to:
```txt
langchain==0.1.20
langchain-community==0.0.38
langchain-openai==0.1.7
PyPDF2==3.0.1
python-dotenv==1.0.0
streamlit==1.29.0
openai==1.30.1
faiss-cpu==1.7.4
tiktoken==0.5.2
```

Then reinstall:
```bash
pip uninstall langchain langchain-community langchain-openai openai -y
pip install -r requirements.txt
```

### Why This Happened

The original `requirements.txt` used:
- `langchain-community` for embeddings and chat models
- Older versions that are incompatible

The **fixed version** uses:
- `langchain-openai` - dedicated package for OpenAI integrations
- Updated compatible versions
- Proper import paths

---

## Error: "No module named 'langchain_openai'"

### Solution
```bash
pip install langchain-openai==0.1.7
```

---

## Error: "OpenAI API key not found"

### Symptoms
- App starts but crashes when processing PDFs
- Error message about API key

### Solutions

**Local Development:**
1. Check `.env` file exists in project root
2. Verify format:
   ```
   OPENAI_API_KEY=sk-proj-xxxxxxxxxxxxx
   ```
3. No quotes around the key
4. No spaces around `=`

**Streamlit Cloud:**
1. Go to app settings
2. Click "Secrets"
3. Add:
   ```toml
   OPENAI_API_KEY = "sk-proj-xxxxxxxxxxxxx"
   ```

**Google Colab:**
- Re-run the cell that asks for API key
- Make sure you copied the full key

---

## Error: "Rate limit exceeded"

### What This Means
You've hit OpenAI's rate limits for your API key.

### Solutions
1. **Wait a few minutes** - Limits reset over time
2. **Check your usage**: https://platform.openai.com/usage
3. **Upgrade your OpenAI plan** if needed
4. **Use smaller PDFs** for testing

---

## Error: "Module not found" Errors

### For any missing module:

```bash
# Activate virtual environment first
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows

# Then install
pip install -r requirements.txt
```

### Common Missing Modules

**tiktoken:**
```bash
pip install tiktoken==0.5.2
```

**faiss-cpu:**
```bash
pip install faiss-cpu==1.7.4
```

**PyPDF2:**
```bash
pip install PyPDF2==3.0.1
```

---

## Error: "Streamlit command not found"

### Symptoms
When you run `streamlit run app.py`, you get "command not found"

### Solution

**Make sure virtual environment is activated:**
```bash
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows
```

**Verify Streamlit is installed:**
```bash
pip list | grep streamlit
```

**If not installed:**
```bash
pip install streamlit==1.29.0
```

---

## Error: PDF Processing Fails

### Symptoms
- "Error processing documents"
- Processing hangs
- No pages extracted

### Solutions

1. **Check PDF is text-based** (not scanned image)
   - Try selecting text in the PDF
   - If you can't select text, it's an image PDF
   - Use OCR tools first

2. **Check PDF isn't corrupted**
   - Try opening in Adobe Reader
   - Re-download if needed

3. **Check file size**
   - Very large PDFs (>50MB) may timeout
   - Try smaller PDFs first

---

## Error: "Port already in use"

### Symptoms
```
OSError: [Errno 48] Address already in use
```

### Solutions

**Option 1: Use different port**
```bash
streamlit run app.py --server.port 8502
```

**Option 2: Kill existing process**

**Mac/Linux:**
```bash
lsof -ti:8501 | xargs kill -9
```

**Windows:**
```bash
netstat -ano | findstr :8501
taskkill /PID [PID_NUMBER] /F
```

---

## Error: Citations Not Showing

### Symptoms
- Answers appear but no "Sources:" section
- Missing page numbers

### Debugging Steps

1. **Check the response in terminal**
   - Look at Streamlit terminal output
   - Should see `source_documents` in response

2. **Verify metadata preservation**
   - Open `app.py`
   - Check `get_pdf_text_with_metadata()` function
   - Should create `Document` objects with metadata

3. **Re-download latest version**
   - The fixed version has this working correctly

---

## Error: "Memory Error" or App Crashes

### Symptoms
- App crashes during processing
- "Out of memory" errors

### Solutions

1. **Process fewer/smaller PDFs**
2. **Reduce chunk size** in `app.py`:
   ```python
   chunk_size=500,  # Instead of 1000
   ```
3. **Close other applications**
4. **Use Streamlit Cloud** instead of local

---

## Google Colab Specific Issues

### ngrok Tunnel Failed

**Solution:**
- Verify authtoken is correct
- Get new token: https://dashboard.ngrok.com/get-started/your-authtoken
- Re-run the ngrok setup cell

### Colab Disconnected

**Solution:**
- Colab free tier times out after inactivity
- Keep the tab active
- Consider upgrading to Colab Pro

### Slow Performance

**Normal on free tier!**
- Processing takes 30-60 seconds
- Wait patiently
- For faster performance, use local or Streamlit Cloud

---

## Streamlit Cloud Specific Issues

### App Won't Deploy

**Check:**
1. `requirements.txt` is in repo root
2. `app.py` is in repo root
3. No syntax errors in code
4. Check build logs for specific errors

### App Crashes After Deployment

**Most Common: Missing API Key**
1. Go to app settings
2. Add OpenAI key to Secrets
3. Reboot app

---

## Still Having Issues?

### Debugging Steps

1. **Check Python version**
   ```bash
   python --version  # Should be 3.8+
   ```

2. **Fresh install**
   ```bash
   # Delete venv
   rm -rf venv
   # Recreate
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

3. **Check all imports work**
   ```python
   python -c "from langchain_openai import OpenAIEmbeddings; print('OK')"
   ```

### Get Help

1. **Check existing issues**: https://github.com/AIdoAI/syllabus-gpt/issues
2. **Open new issue** with:
   - Error message (full traceback)
   - Python version
   - Operating system
   - Steps to reproduce

---

## Version Compatibility Matrix

| Package | Version | Notes |
|---------|---------|-------|
| Python | 3.8 - 3.11 | Required |
| langchain | 0.1.20 | Fixed version |
| langchain-community | 0.0.38 | Fixed version |
| langchain-openai | 0.1.7 | **Important!** |
| openai | 1.30.1 | Compatible version |
| streamlit | 1.29.0 | Tested version |

**Use these exact versions** to avoid compatibility issues!

---

## Quick Health Check

Run this to verify your setup:

```python
# test_setup.py
import sys
print(f"Python: {sys.version}")

try:
    import streamlit
    print(f"✅ Streamlit: {streamlit.__version__}")
except ImportError as e:
    print(f"❌ Streamlit: {e}")

try:
    from langchain_openai import OpenAIEmbeddings, ChatOpenAI
    print("✅ langchain-openai: OK")
except ImportError as e:
    print(f"❌ langchain-openai: {e}")

try:
    from langchain_community.vectorstores import FAISS
    print("✅ langchain-community: OK")
except ImportError as e:
    print(f"❌ langchain-community: {e}")

try:
    import openai
    print(f"✅ OpenAI: {openai.__version__}")
except ImportError as e:
    print(f"❌ OpenAI: {e}")

print("\nIf all show ✅, you're good to go!")
```

Run: `python test_setup.py`

---

**Most issues are solved by using the updated `requirements.txt` with compatible versions!**
