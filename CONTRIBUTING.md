# Contributing to Syllabus-GPT

First off, thank you for considering contributing to Syllabus-GPT! 

## Code of Conduct

This project adheres to a simple principle: be respectful, be helpful, be constructive.

## How Can I Contribute?

### Reporting Bugs

Before creating bug reports, please check existing issues. When creating a bug report, include:

- **Clear title and description**
- **Steps to reproduce** the issue
- **Expected vs actual behavior**
- **Screenshots** if applicable
- **Environment details** (OS, Python version, etc.)

### Suggesting Enhancements

Enhancement suggestions are tracked as GitHub issues. When creating an enhancement suggestion, include:

- **Clear use case**: What problem does this solve?
- **Proposed solution**: How would this work?
- **Alternatives considered**: What other approaches did you think about?

### Pull Requests

1. Fork the repo and create your branch from `main`
2. Make your changes
3. Update documentation if needed
4. Write clear commit messages
5. Submit a pull request

## Development Setup

```bash
# Fork and clone
git clone https://github.com/YOUR_USERNAME/syllabus-gpt.git
cd syllabus-gpt

# Create branch
git checkout -b feature/amazing-feature

# Setup environment
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Create .env
cp .env.example .env
# Add your OPENAI_API_KEY
```

## Code Style

- Follow PEP 8 guidelines
- Use meaningful variable names
- Add docstrings to functions
- Keep functions focused and small
- Comment complex logic

### Example:
```python
def get_pdf_text_with_metadata(pdf_docs):
    """
    Extract text from PDFs while preserving metadata about source and page numbers.
    
    Args:
        pdf_docs (list): List of uploaded PDF file objects
        
    Returns:
        list: List of Document objects with content and metadata
    """
    # Implementation...
```

## Testing Guidelines

Before submitting:

1. Test with sample course PDFs
2. Verify source citations are accurate
3. Check UI displays correctly
4. Ensure error handling works
5. Test with multiple documents

## Documentation

Update relevant documentation when making changes:

- README.md - For feature changes
- CHANGELOG.md - Document all changes
- SETUP.md - For installation changes
- Code comments - For complex logic

## Commit Messages

Use clear, descriptive commit messages:

**Good:**
- `feat: add support for DOCX files`
- `fix: correct page number indexing in citations`
- `docs: update installation instructions`

**Bad:**
- `update stuff`
- `fixed bug`
- `changes`

## Areas Where Help Is Needed

### High Priority
- [ ] Support for other document formats (DOCX, PPTX)
- [ ] Export chat history feature
- [ ] Improved error handling for corrupt PDFs
- [ ] Mobile-responsive UI improvements

### Medium Priority
- [ ] Add usage analytics
- [ ] Implement caching for common queries
- [ ] Add more LLM provider options (Claude, Cohere)
- [ ] Create video tutorial

### Low Priority
- [ ] Dark mode theme
- [ ] Multi-language support
- [ ] Browser extension
- [ ] Desktop app version

## Questions?

Feel free to open an issue with the `question` label!

## Recognition

Contributors will be recognized in:
- README.md Contributors section
- CHANGELOG.md for specific contributions
- GitHub contributors page

Thank you for contributing! 🎓
