import streamlit as st
from parser.extractor import extract_fields
from parser.matcher import suggest_roles
import tempfile

st.set_page_config(page_title="Smart Resume Parser", layout="centered")
st.title("📄 Smart Resume Parser & Job Matcher")
st.write("Upload a resume PDF to extract key information and get matched to suitable job roles.")

uploaded_file = st.file_uploader("Upload Resume (PDF)", type="pdf")

if uploaded_file is not None:
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        tmp.write(uploaded_file.read())
        file_path = tmp.name

    with st.spinner("Extracting fields..."):
        extracted = extract_fields(file_path)
        suggested_roles = suggest_roles(extracted["Skills"])
        extracted["Suggested Roles"] = suggested_roles

    st.subheader("📋 Extracted Information")
    st.json(extracted)
