# 🎯 Quick Demo Creation - 10 Minute Guide

**Goal:** Get a demo screenshot of Syllabus-GPT in 10 minutes using Google Colab

---

## ✅ What You Need (Get These First!)

1. **OpenAI API Key**
   - Go to: https://platform.openai.com/api-keys
   - Click "Create new secret key"
   - Copy it (starts with `sk-`)
   - **Save it somewhere** - you won't see it again!

2. **ngrok Account** (Free)
   - Go to: https://ngrok.com
   - Sign up (free)
   - Go to: https://dashboard.ngrok.com/get-started/your-authtoken
   - Copy your authtoken
   - **Save it** - looks like: `2abc...XYZ`

---

## 📝 Step-by-Step Instructions

### Step 1: Open Google Colab (1 minute)
1. Go to: https://colab.research.google.com/
2. Click "File" → "Upload notebook"
3. Upload `Syllabus_GPT_Colab.ipynb` (from the zip file you downloaded)

### Step 2: Run the Notebook (5 minutes)
1. Click "Runtime" → "Run all"
2. **When prompted for OpenAI key:** Paste your API key
3. **When prompted for ngrok token:** Paste your authtoken
4. Wait for the cells to finish running
5. Look for the ngrok URL (appears like: `https://xxxx.ngrok-free.app`)

### Step 3: Access Syllabus-GPT (1 minute)
1. **Click the ngrok URL**
2. You might see an ngrok warning page:
   - Click "Visit Site" button
3. Syllabus-GPT should load!

### Step 4: Upload Sample Syllabus (2 minutes)
1. In the **sidebar**, click "Browse files"
2. Select the sample PDF:
   - If you cloned the repo: `examples/sample_syllabi/CS301_AI_Syllabus.pdf`
   - Or use the standalone `sample_syllabus.pdf` file
3. Click **"🔄 Process Documents"**
4. Wait 20-30 seconds for processing

### Step 5: Ask Question & Screenshot (1 minute)
1. In the text input, type: **"What is the grading breakdown for this course?"**
2. Press Enter
3. Wait for the answer (with citations!)
4. Take a screenshot:
   - **Mac:** `Cmd + Shift + 4` → drag to select
   - **Windows:** `Windows + Shift + S` → select area
5. **Make sure your screenshot includes the citation!**
   - Should show: `📄 CS301_AI_Syllabus.pdf (p. 1)`

---

## 📸 Perfect Screenshot Checklist

Your screenshot should show:
- [ ] The "🎓 Syllabus-GPT" header
- [ ] Your question in the input box
- [ ] The AI's complete answer
- [ ] **The source citation** (most important!)
- [ ] The sidebar (showing uploaded documents)

---

## 💡 Tips

**If processing takes too long:**
- Colab free tier can be slow
- Wait patiently (up to 1 minute)
- If it errors, try again

**If ngrok URL doesn't work:**
- Check you entered the authtoken correctly
- Try copying it again from ngrok dashboard
- Re-run the ngrok cell

**If answer has no citations:**
- This means something's wrong with the code
- Try asking a different question
- Or reload and try again

---

## 🎨 Example Screenshots to Inspire You

### Good Screenshot Shows:
```
┌─────────────────────────────────────┐
│ 🎓 Syllabus-GPT                     │
├─────────────────────────────────────┤
│ Ask: What is the grading breakdown? │
│                                      │
│ Answer:                              │
│ The grading is:                      │
│ • Homework: 30%                      │
│ • Midterm: 25%                       │
│ • Final Project: 30%                 │
│ • Participation: 10%                 │
│ • Quizzes: 5%                        │
│                                      │
│ Sources:                             │
│ 📄 CS301_AI_Syllabus.pdf (p. 1)    │
└─────────────────────────────────────┘
```

---

## 🚀 After Getting Your Screenshot

1. **Save it as** `demo.png`
2. **Add to your GitHub repo:**
   ```bash
   git add demo.png
   git commit -m "Add demo screenshot"
   git push
   ```
3. **Update README if needed** (already has placeholder)

---

## ⏱️ Timeline

- **Minute 0-1:** Get API keys
- **Minute 1-2:** Upload notebook to Colab
- **Minute 2-7:** Run all cells, enter keys
- **Minute 7-8:** Access app via ngrok URL
- **Minute 8-9:** Upload PDF and process
- **Minute 9-10:** Ask question & screenshot!

**Total: 10 minutes** ✅

---

## 🆘 Quick Troubleshooting

| Problem | Solution |
|---------|----------|
| Can't find API key | Go to https://platform.openai.com/api-keys |
| ngrok URL broken | Re-run Step 4 cell in Colab |
| Processing failed | Check your API key has credits |
| No citations showing | Try a different question or reload |

---

## 📌 Alternative: Streamlit Cloud (For Later)

Once your GitHub repo is live, you can deploy to Streamlit Cloud:
- Go to: https://share.streamlit.io
- Connect your GitHub repo
- Get a permanent public URL!
- See `DEPLOYMENT.md` for full instructions

---

**You're all set! Time to create that demo! 🎓**
