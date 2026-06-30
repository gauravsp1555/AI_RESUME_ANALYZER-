import google.generativeai as genai
import os
import ast
import json
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("GEMINI API KEY NOT FOUND IN ENV")

# Configure the Google GenAI SDK with the retrieved API key
genai.configure(api_key=api_key)

# Initialize the Gemini model with a configuration to strictly enforce JSON output
model = genai.GenerativeModel(
    'gemini-2.5-flash',
    generation_config={"response_mime_type": "application/json"}
)

def extract_skill_with_gemini(resume_text):
    """
    Parses raw resume text and uses Gemini API to extract a clean list of technical skills.
    """
    prompt = f"""
    From the given resume text, extract a clean JSON list of technical skills only.
    Return ONLY a valid JSON array of strings. Do not include any markdown wrappers or text.

    Resume Text:
    {resume_text}
    """
    response = model.generate_content(prompt)
    
    try:
        # Safely parse the structured JSON response into a Python list
        skills = json.loads(response.text.strip())
    except Exception as e:
        skills = []
        print("Gemini response error:", e)
        print("Raw Response was:", response.text)  # Log the raw response for fallback debugging
    
    return skills

def generate_suggestions_with_gemini(job_role, matched_skills, missing_skills, score):
    """
    Generates personalized career advisor suggestions and textual insights based on skill gaps.
    """
    # Using a standard configuration instance here as paragraph text output is expected
    text_model = genai.GenerativeModel('gemini-2.5-flash')
    prompt = f"""
You are a career advisor AI.

Given this information:
- Job Role: {job_role}
- Skills the candidate already has: {matched_skills}
- Skills missing: {missing_skills}
- Current match score: {score}%

Provide personalized, detailed improvement suggestions to help the candidate improve their resume and skillset for the role of a {job_role}. 
Focus on missing skills, suggest resources, and explain what to learn next.
Output in 2-3 short paragraphs.
"""
    response = text_model.generate_content(prompt)
    return response.text.strip()

def get_required_skills_from_gemini(job_role: str):
    """
    Dynamically fetches the top 10 standard technical skills for an undefined job role using Gemini.
    """
    prompt = f"List 10 most important technical skills required for a {job_role}. Return only as a JSON list of strings."
    
    try:
        response = model.generate_content(prompt)
        skills = json.loads(response.text.strip())
        return skills
    except Exception as e:
        print("Gemini response error:", e)
        return []