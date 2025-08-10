# Smart_Resume_Parser-Job_Matcher
An Atomated system that automatically extracts key details from resumes (skills, experience, education) and matches candidates to the most relevant job openings based on their profile. Helps recruiters save time and improves hiring accuracy.

# Smart Resume Parser & Job Matcher (Streamlit Version)

An interactive Streamlit web app to:
- Extract fields (name, email, skills) from resumes
- Match skills to most relevant job roles using semantic similarity

## 📦 How to Run
```bash
pip install -r requirements.txt
streamlit run app.py
```

## 📁 Project Structure
- `app.py`: Streamlit web interface
- `parser/`: Logic for text extraction and role matching
- `resumes/`: Store sample resumes
- `roles/`: Contains job role descriptions in JSON

## ✅ Demo Output
```json
{
  "Name": "Ananya Sharma",
  "Email": "ananya.sharma@gmail.com",
  "Skills": ["Python", "PyTorch", "FastAPI"],
  "Suggested Roles": [
    {"title": "Machine Learning Engineer", "match_score": 91.2},
    {"title": "Product Manager", "match_score": 78.5}
  ]
}
```

