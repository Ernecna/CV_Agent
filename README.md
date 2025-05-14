# 📄 HireGraph

## 🚀 Project Overview

**HireGraph** is a modular Python project that uses LLM-powered agents to evaluate candidate CVs step by step against a job description. It analyzes the candidate’s skills, experience, and project relevance to provide individual scores and a concise final summary.

Built on top of Google’s **Gemini** language models and the **LangGraph** framework, this system enables structured, interpretable, and extensible evaluation of resumes.

---

## 🎯 Goal

Evaluate a CV from three key perspectives:

- ✅ **Skill Match**
- ✅ **Experience Relevance**
- ✅ **Project Alignment**

And then generate:

- 📊 A total weighted score (out of 100)
- 📝 A 200–300 character final summary statement

---

## 🧠 Tech Stack

| Technology       | Purpose                               |
|------------------|----------------------------------------|
| **LangGraph**    | Multi-step agent pipeline              |
| **Gemini API**   | LLM-powered natural language analysis  |
| **Tesseract OCR**| Convert PDF CVs to readable text       |
| **Python**       | Clean, modular, scalable implementation|

---

## 🧱 Project Structure

cv_reader/
├── main.py # Entry point – runs the pipeline
├── ocr_reader.py # OCR module for PDF CVs
├── llm_client.py # Gemini LLM API interaction
├── langgraph_pipeline.py # LangGraph-based agent workflow
├── data/
│ └── sample_cv.pdf # Example candidate CV
└── README.md

yaml
Copy
Edit

---

## ⚙️ Installation

```bash
# Create a virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
⚠️ Note: You must install Tesseract separately
🔗 Tesseract installation guide

▶️ Running the Project
bash
Copy
Edit
python main.py
📥 Input
sample_cv.pdf: A candidate’s CV in PDF format

job_posting: The job description, provided as text in main.py

📤 Output
Per-step evaluations:

Skill Analysis

Experience Analysis

Project Analysis

Final Output:

Total Score (0–100)

Short Summary (200–300 characters)

🚧 Future Improvements
🔄 Support for evaluating multiple CVs (batch mode)

⚖️ Customizable weighting per evaluation category

🧾 Auto-detection of CV sections

🌐 Web interface (Flask, Streamlit, etc.)

📄 License
MIT License – open source, free to use and contribute to.
