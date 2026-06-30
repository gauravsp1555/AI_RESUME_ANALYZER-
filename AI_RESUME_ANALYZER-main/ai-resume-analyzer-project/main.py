import shutil
import os
from fastapi import FastAPI, File, UploadFile, Form
from gemini_utils import extract_skill_with_gemini, generate_suggestions_with_gemini, get_required_skills_from_gemini
from model import match_skills_dynamic
from job_roles import job_roles
from utils import extract_text_from_resume
from graph_utils import generate_skill_match_graph

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to Resume Analyzer"}

# Ensure temporary upload directory exists
os.makedirs("temp_upload", exist_ok=True)

@app.post("/analyze")
async def analyze_resume(file: UploadFile = File(...), job_role: str = Form(...)):
    temp_fpath = f"temp_upload/{file.filename}"
    
    # Save the uploaded file temporarily to the server
    with open(temp_fpath, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Extract text content from the uploaded resume file
    text = extract_text_from_resume(temp_fpath)
    
    # --- DEBUGGING AND LOGGING SECTION ---
    print("\n--- DEBUG START ---")
    print(f"Extracted Text Length: {len(text)}")
    print(f"Sample Text (First 500 chars): {text[:500]}")
    
    # Leverage Gemini API to parse and extract technical skills
    user_skills = extract_skill_with_gemini(text)
    print(f"Gemini Returned Skills: {user_skills}")
    print("--- DEBUG END ---\n")
    # -------------------------------------

    # Handle cases where no technical skills could be extracted
    if not user_skills or len(user_skills) == 0:
        os.remove(temp_fpath)
        return {
            "error": "No skills found in the resume. Please upload a more detailed resume with technical or relevant skills mentioned."
        }

    # Fetch required skills either from local configuration or dynamically via Gemini
    if job_role.lower() in job_roles:
        required_skills = job_roles[job_role.lower()]
    else:
        required_skills = get_required_skills_from_gemini(job_role)

    # Process skill matching logic, generate analytical graph, and get AI suggestions
    matched, missing, score = match_skills_dynamic(user_skills, required_skills)
    graph_img = generate_skill_match_graph(matched, missing)
    suggestions = generate_suggestions_with_gemini(job_role, matched, missing, score)
    
    # Clean up the temporary file from the storage
    os.remove(temp_fpath)

    # Return structured analytical response
    return {
        "job_role": job_role,
        "match_score": f"{score}%",
        "matched_skills": matched,
        "missing_skills": missing,
        "your_skills": user_skills,
        "required_skills": required_skills,
        "skill_graph_base64": graph_img,
        "ai_suggestions": suggestions
    }