import streamlit as st
import requests
import PyPDF2

st.set_page_config(page_title="AI Cover Letter Generator", layout="wide")

# Sidebar (UI style like ChatGPT)
st.sidebar.title("History")
st.sidebar.write("Previous Sessions")
st.sidebar.write("- Cover Letter 1")
st.sidebar.write("- Cover Letter 2")

st.title("AI Personalized Cover Letter Generator")

# User Inputs
name = st.text_input("Enter Your Name")
job_role = st.text_input("Job Role Applying For")
company = st.text_input("Company Name")

job_description = st.text_area("Paste Job Description (Optional)")

uploaded_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])

if st.button("Generate Cover Letter"):

    if not (name and job_role and company and uploaded_file):
        st.warning("Please fill all required fields and upload resume.")
    else:
        # Extract text from PDF
        pdf_reader = PyPDF2.PdfReader(uploaded_file)
        resume_text = ""

        for page in pdf_reader.pages:
            resume_text += page.extract_text()

        # Create AI Prompt
        prompt = f"""
        Write a professional and personalized cover letter.

        Candidate Name: {name}
        Job Role: {job_role}
        Company: {company}

        Resume Details:
        {resume_text}

        Job Description:
        {job_description}

        Make it formal and professional.
        """

        # Send to Ollama
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "mistral",
                "prompt": prompt,
                "stream": False
            }
        )

        result = response.json()

        st.subheader("Generated Cover Letter")
        st.text_area("", result["response"], height=400)