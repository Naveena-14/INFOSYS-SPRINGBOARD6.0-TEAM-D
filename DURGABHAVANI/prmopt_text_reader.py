import streamlit as st
import pytesseract
from PIL import Image
import requests
import fitz  # PyMuPDF for PDF reading

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

st.set_page_config(layout="wide")

st.title("Personalized Cover Letter Generator")

# -------- SESSION STATE --------
if "history" not in st.session_state:
    st.session_state.history = []

if "resume_text" not in st.session_state:
    st.session_state.resume_text = ""

if "job_description_text" not in st.session_state:
    st.session_state.job_description_text = ""

# -------- SIDEBAR HISTORY --------
st.sidebar.title("History")

if st.session_state.history:
    for i, letter in enumerate(st.session_state.history):
        if st.sidebar.button(f"Cover Letter {i+1}", key=i):
            st.session_state.selected_letter = letter
else:
    st.sidebar.write("No history yet")

# -------- USER INPUT --------
candidate_name = st.text_input("Enter Your Name")
company_name = st.text_input("Enter Company Name")
job_role = st.text_input("Enter Job Role")

st.subheader("Upload Resume and Job Description")

uploaded_files = st.file_uploader(
    "Upload files (Image, PDF, TXT)",
    type=["png", "jpg", "jpeg", "pdf", "txt"],
    accept_multiple_files=True
)

# -------- PROCESS FILES --------
if uploaded_files:

    for file in uploaded_files:

        st.write(f"File: {file.name}")

        file_type = st.selectbox(
            f"Select type for {file.name}",
            ["Resume", "Job Description"],
            key=file.name
        )

        extracted_text = ""

        # Image OCR
        if file.type.startswith("image"):
            image = Image.open(file)
            extracted_text = pytesseract.image_to_string(image)

        # Text file
        elif file.type == "text/plain":
            extracted_text = file.read().decode("utf-8")

        # PDF file
        elif file.type == "application/pdf":
            pdf = fitz.open(stream=file.read(), filetype="pdf")
            for page in pdf:
                extracted_text += page.get_text()

        # Store based on selection
        if file_type == "Resume":
            st.session_state.resume_text = extracted_text

        elif file_type == "Job Description":
            st.session_state.job_description_text = extracted_text

        st.subheader(f"Extracted Text from {file.name}")
        st.write(extracted_text)

# -------- GENERATE COVER LETTER --------
if st.button("Generate Cover Letter"):

    if (
        st.session_state.resume_text.strip() == ""
        or st.session_state.job_description_text.strip() == ""
        or candidate_name.strip() == ""
        or company_name.strip() == ""
        or job_role.strip() == ""
    ):
        st.warning("Please upload Resume and Job Description and fill all fields")

    else:

        prompt = f"""
Write a professional cover letter for:

Candidate Name: {candidate_name}
Applying for: {job_role}
Company: {company_name}

Resume Details:
{st.session_state.resume_text}

Job Description:
{st.session_state.job_description_text}

Make it professional, concise, and personalized.
"""

        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "llama3",
                "prompt": prompt,
                "stream": False
            }
        )

        result = response.json()

        cover_letter = result["response"]

        st.subheader("Generated Cover Letter")
        st.write(cover_letter)

        # Save history
        st.session_state.history.append(cover_letter)

# -------- SHOW SELECTED HISTORY --------
if "selected_letter" in st.session_state:
    st.subheader("Selected from History")
    st.write(st.session_state.selected_letter)
