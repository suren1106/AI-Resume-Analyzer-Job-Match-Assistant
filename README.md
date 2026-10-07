# 🤖 AI Resume Analyzer & Job Match Assistant

An **LLM-powered Generative AI application** that analyzes a candidate's resume against a job description and provides intelligent insights including skill matching, missing skills, experience gaps, resume improvement suggestions, technical interview questions, and a role-specific professional summary.

Built with **Python, Streamlit, Hugging Face Inference Providers, and GPT-OSS**.

---

## 🚀 Project Overview

Recruiters and candidates often need to quickly understand how well a resume matches a specific job description.

This project uses **Generative AI and prompt engineering** to automate that analysis.

### Input

- Candidate Resume
- Job Description

### Output

- Match Score
- Matching Skills
- Missing Skills
- Experience Gaps
- Resume Improvement Suggestions
- Technical Interview Questions
- Job-Specific Professional Summary

---

## 🧠 Architecture

```text
                  ┌──────────────────┐
                  │     Resume       │
                  └────────┬─────────┘
                           │
                           │
                  ┌────────▼─────────┐
                  │ Job Description  │
                  └────────┬─────────┘
                           │
                           ▼
                 ┌────────────────────┐
                 │ Prompt Engineering │
                 └─────────┬──────────┘
                           │
                           ▼
                 ┌────────────────────┐
                 │    LLM Inference   │
                 │   GPT-OSS Model    │
                 └─────────┬──────────┘
                           │
                           ▼
                 ┌────────────────────┐
                 │ AI Analysis        │
                 ├────────────────────┤
                 │ Match Score        │
                 │ Matching Skills    │
                 │ Missing Skills     │
                 │ Experience Gap     │
                 │ Improvements       │
                 │ Interview Questions│
                 │ Professional       │
                 │ Summary            │
                 └────────────────────┘
```

---

# ✨ Key Features

### 📊 Resume–Job Matching

Analyzes the relationship between the candidate's skills and the job requirements.

### 🎯 Skill Gap Analysis

Identifies important skills mentioned in the job description that are not clearly demonstrated in the resume.

### 🧠 Context-Aware Generation

The LLM receives both the resume and job description as context before generating the analysis.

### 🛡️ Hallucination Reduction

The prompt explicitly instructs the model not to invent:

- Skills
- Experience
- Certifications
- Projects
- Technologies

### 💼 Interview Question Generation

Generates technical interview questions based on the target role and candidate background.

### ✍️ AI Resume Enhancement

Generates practical suggestions for improving the resume for the target position.

### 📥 Downloadable Report

Users can download the generated analysis as a text file.

### 💻 Lightweight Architecture

The application does not require a local GPU or local LLM.

Inference is performed through a hosted LLM API, making the project suitable for low-specification systems.

---

# 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Python | Application development |
| Streamlit | Web application |
| Hugging Face | LLM inference |
| GPT-OSS | Generative AI |
| Open
