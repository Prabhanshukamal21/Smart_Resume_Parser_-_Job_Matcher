# Smart_Resume_Parser-Job_Matcher
An Atomated system that automatically extracts key details from resumes (skills, experience, education) and matches candidates to the most relevant job openings based on their profile. Helps recruiters save time and improves hiring accuracy.

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
"Name":"Prabhanshukamal Ahirwar"
"Email":"prabhanshu2108@gmail.com"
"Phone":"+91 9691848220"
"Skills":[
0:"Languages and Databases: Python"
1:"C++"
2:"SQL"
]
"RawText":"Prabhanshukamal Ahirwar 
                    
 +91 9691848220           prabhanshu2108@gmail.com  
https://github.com/Prabhanshukamal21 
Technical Skills 
 
Languages and Databases: Python, R, C/C++, SQL 
Visualization Tools: Tableau, Power BI, Matplotlib, Seaborn 
Other Skills: Advanced Excel, Business Analysis, Customer Acquisition  
Frontend & Backend: HTML5, CSS3, javascript, ReactJs, Tailwind CSS, Bootstrap and Node js, Express 
Frameworks: pandas, numpy, scikit-learn, matplotlib, seaborn, "
"Suggested Roles":[
0:{
"title":"Machine Learning Engineer"
"match_score":35.68
}
1:{
"title":"Web Developer"
"match_score":20.9
}
2:{
"title":"Project Manager"
"match_score":14.8
}
]
}

