# About the Demo Screenshot

## Why is `demo.png` Missing?

The README.md references `demo.png` (a screenshot of Syllabus-GPT in action), but this file doesn't exist yet because:

1. **You need to run the app first** - The screenshot should show YOUR actual working application
2. **It's better to be authentic** - A real screenshot shows the app actually works
3. **Screenshots are environment-specific** - They look different on different computers

## How to Create demo.png

### Method 1: Run Locally and Screenshot (Recommended)

#### Step 1: Run Syllabus-GPT
```bash
# Navigate to project
cd syllabus-gpt

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Create .env file with your OpenAI API key
echo "OPENAI_API_KEY=your_key_here" > .env

# Run the app
streamlit run app.py
```

#### Step 2: Upload Sample PDF
1. In the sidebar, click "Browse files"
2. Upload `examples/sample_syllabi/CS301_AI_Syllabus.pdf`
3. Click "🔄 Process Documents"
4. Wait for processing to complete

#### Step 3: Ask a Question
Type in the input box: "What is the grading breakdown for this course?"

#### Step 4: Take Screenshot
**On Mac:**
- Press `Cmd + Shift + 4`
- Click and drag to select the area
- Screenshot saves to Desktop

**On Windows:**
- Press `Windows + Shift + S`
- Select area
- Save from clipboard

#### Step 5: Save and Add to Repo
1. Save screenshot as `demo.png`
2. Place it in the root of `syllabus-gpt/` folder
3. Commit and push to GitHub:
   ```bash
   git add demo.png
   git commit -m "Add demo screenshot"
   git push origin main
   ```

### Method 2: Use GitHub's Social Preview Instead

If you don't want to include a demo.png in your repo, you can:

1. **Remove the reference in README.md:**
   - Delete or comment out the line: `![Syllabus-GPT Interface](demo.png)`

2. **Use GitHub's social preview feature:**
   - Go to your repo settings
   - Scroll to "Social preview"
   - Upload an image there
   - This shows when sharing on social media

### Method 3: Create a Simple Mockup

If you can't run the app yet, you can:

1. Create a simple image in Canva/Figma showing:
   - The app name "Syllabus-GPT"
   - A question input box
   - An answer with citation
   - The sidebar with upload button

2. Label it clearly as a "mockup" or "coming soon"

## What Should the Screenshot Show?

For maximum impact, your screenshot should include:

✅ **The full interface:**
- Header: "🎓 Syllabus-GPT"
- Question input box
- At least one complete Q&A exchange
- **Most importantly: SOURCE CITATIONS visible** (this is your key feature!)
- Sidebar showing uploaded documents

✅ **Good example Q&A to show:**
```
Q: What is the grading breakdown?

A: The grading breakdown is:
- Homework Assignments: 30%
- Midterm Exam: 25%
- Final Project: 30%
- Class Participation: 10%
- Quizzes: 5%

Sources:
📄 CS301_AI_Syllabus.pdf (p. 1)
```

## Tips for a Great Screenshot

1. **Use the sample syllabus** - It has clear, easy-to-read answers
2. **Show the citations** - This is what makes your project unique!
3. **Clean browser window** - Close unnecessary tabs
4. **Good lighting** - Make sure text is readable
5. **Crop appropriately** - Focus on the app, not browser chrome

## Alternative: GIF Instead of Screenshot

Even better than a static image, you could create an animated GIF showing:
1. Uploading a PDF
2. Processing
3. Asking a question
4. Getting an answer with citations

**Tools for creating GIFs:**
- **Mac**: Kap (free) - https://getkap.co/
- **Windows**: ScreenToGif (free)
- **Online**: Loom (records, converts to GIF)

## Current Status

📝 **README.md has a placeholder** for `demo.png` at line ~47:
```markdown
## 📸 Demo

![Syllabus-GPT Interface](demo.png)
```

**Options:**
1. ✅ **Keep it** - Add screenshot when ready
2. ✅ **Remove it** - Delete those lines from README
3. ✅ **Replace with text** - Describe what users will see instead

## Quick Fix: Remove the Reference

If you want to push to GitHub now without a screenshot:

```bash
# Edit README.md and remove these lines:
## 📸 Demo

![Syllabus-GPT Interface](demo.png)
```

Or replace with:
```markdown
## 📸 Demo

*Screenshot coming soon - run the app locally to see it in action!*
```

---

**Bottom line:** It's totally fine to push to GitHub without demo.png. You can add it later when you run the app!
