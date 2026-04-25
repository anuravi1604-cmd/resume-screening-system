import streamlit as st
from utils import compute_match, extract_keywords, missing_keywords
import PyPDF2

st.set_page_config(page_title="AI Resume Screening System", layout="centered")

st.title("📄 AI Resume Screening System")
st.markdown("Analyze resume-job fit using NLP and similarity scoring")

st.divider()

# Upload section
uploaded_file = st.file_uploader("Upload Resume (PDF or TXT)", type=["pdf", "txt"])

resume_text = ""

if uploaded_file:
    if uploaded_file.type == "application/pdf":
        pdf_reader = PyPDF2.PdfReader(uploaded_file)
        for page in pdf_reader.pages:
            if page.extract_text():
                resume_text += page.extract_text()
    else:
        resume_text = uploaded_file.read().decode("utf-8")

# Manual input
resume_input = st.text_area("Or paste resume text", height=150)
jd_text = st.text_area("Paste Job Description", height=200)

if resume_input:
    resume_text = resume_input

st.divider()

# Analyze button
if st.button("🔍 Analyze Resume"):
    if not resume_text or not jd_text:
        st.warning("Please provide both resume and job description")
    else:
        score = compute_match(resume_text, jd_text)
        keywords = extract_keywords(resume_text, jd_text)
        missing = missing_keywords(resume_text, jd_text)

        # Score
        st.subheader("📊 Match Score")
        st.progress(int(score))
        st.success(f"{score}% match")

        # Preview
        st.subheader("📄 Resume Preview")
        st.text(resume_text[:500])

        # Keywords
        st.subheader("🔑 Matching Keywords")
        if keywords:
            st.write(", ".join(keywords))
        else:
            st.write("No strong keyword overlap found")

        # Missing
        st.subheader("⚠️ Missing Keywords")
        if missing:
            st.write(", ".join(missing))
        else:
            st.write("Good coverage of required skills")

        # Summary
        st.subheader("🧠 Analysis Summary")
        st.write(f"This resume matches {score}% of the job requirements based on keyword and semantic similarity.")

        # Recommendation
        st.subheader("💡 Recommendation")
        if score > 75:
            st.success("Strong match — excellent fit")
        elif score > 40:
            st.info("Moderate match — can improve alignment")
        else:
            st.error("Low match — resume needs optimization")

st.caption("Built using Python, Streamlit, and Scikit-learn")