import json
from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer("all-MiniLM-L6-v2")

with open("roles/job_descriptions.json") as f:
    roles_data = json.load(f)

role_titles = list(roles_data.keys())
role_embeddings = model.encode([roles_data[r] for r in role_titles], convert_to_tensor=True)

def suggest_roles(candidate_skills):
    if not candidate_skills:
        return []
    skill_string = ", ".join(candidate_skills)
    skill_embedding = model.encode(skill_string, convert_to_tensor=True)
    scores = util.cos_sim(skill_embedding, role_embeddings)[0]
    ranked = sorted(zip(role_titles, scores), key=lambda x: x[1], reverse=True)
    return [{"title": r, "match_score": round(float(s)*100, 2)} for r, s in ranked[:3]]
