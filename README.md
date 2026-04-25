# 📄 AI Resume Screening System

An AI-powered web application that analyzes how well a resume matches a job description using Natural Language Processing (NLP) techniques.

---

## 🚀 Live Demo
👉 [https://your-app-name.streamlit.app](https://resume-screening-system-1604.streamlit.app/)

---

## 🧠 Features

- 📄 Upload resume (PDF or TXT)
- ✍️ Paste job description
- 📊 Match score using TF-IDF & cosine similarity
- 🔑 Extract matching keywords
- ⚠️ Identify missing keywords
- 💡 Smart recommendation based on score

---

## 🛠️ Tech Stack

- Python
- Streamlit
- Scikit-learn
- NLP (TF-IDF Vectorization)
- PyPDF2

---

## ⚙️ How It Works

1. Resume and job description text are cleaned and preprocessed
2. TF-IDF vectorization converts text into numerical features
3. Cosine similarity calculates the match score
4. Common keywords and missing skills are identified

---

## 📁 Project Structure
resume-screening/
│── app.py # Streamlit frontend
│── utils.py # NLP + scoring logic
│── requirements.txt # Dependencies
│── README.md

---

## ▶️ Run Locally

git clone https://github.com/anuravi1604-cmd/resume-screening-system.git
cd resume-screening-system
pip install -r requirements.txt
streamlit run app.py
