import fitz  # PyMuPDF
import re

def extract_fields(pdf_path):
    doc = fitz.open(pdf_path)
    text = "\n".join([page.get_text() for page in doc])

    name = re.findall(r"(?i)^([A-Z][a-z]+\s[A-Z][a-z]+)", text)
    email = re.findall(r"[\w\.-]+@[\w\.-]+", text)
    phone = re.findall(r"\+?\d[\d\s\-]{8,}\d", text)
    skills = re.findall(r"(?i)(skills|technologies):?\s*(.*)", text)

    skills_list = []
    if skills:
        skills_line = skills[0][1]
        skills_list = [s.strip() for s in re.split(",|/|\\\\|\||\n", skills_line) if len(s.strip()) > 1]

    return {
        "Name": name[0] if name else "",
        "Email": email[0] if email else "",
        "Phone": phone[0] if phone else "",
        "Skills": skills_list,
        "RawText": text[:500]
    }
