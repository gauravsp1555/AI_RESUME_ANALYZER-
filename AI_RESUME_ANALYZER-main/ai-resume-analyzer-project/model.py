from gemini_utils import get_required_skills_from_gemini

def match_skills_dynamic(user_skills, job_role):
    required_skills = get_required_skills_from_gemini(job_role)
    matched = list(set(user_skills) & set(required_skills))
    missing = list(set(required_skills) - set(user_skills))
    return matched, missing, required_skills
