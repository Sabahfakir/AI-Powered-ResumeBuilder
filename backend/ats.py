import textstat
import re

# ------------------------------
# BASIC ATS (Used in Resume Builder Page)
# ------------------------------
def calculate_ats_score(resume_text, job_description):

    if not resume_text or not job_description:
        return {"ats_score": 0}

    job_words = set(clean_text(job_description).split())
    resume_words = set(clean_text(resume_text).split())

    matches = job_words.intersection(resume_words)

    keyword_score = (len(matches) / len(job_words)) * 70 if job_words else 0
    readability = textstat.flesch_reading_ease(resume_text)
    readability_score = min(30, max(0, readability / 2))

    final_score = round(keyword_score + readability_score, 2)

    return {
        "ats_score": min(100, final_score)
    }


# ------------------------------
# ADVANCED ATS (Upload Page)
# ------------------------------
def calculate_ats_score_advanced(resume_text, job_description):

    job_words = set(clean_text(job_description).split())
    resume_words = set(clean_text(resume_text).split())

    matches = job_words.intersection(resume_words)
    missing = job_words - resume_words

    keyword_score = (len(matches) / len(job_words)) * 70 if job_words else 0
    readability = textstat.flesch_reading_ease(resume_text)
    readability_score = min(30, max(0, readability / 2))

    final_score = round(keyword_score + readability_score, 2)

    return {
        "ats_score": min(100, final_score),
        "keyword_matches": len(matches),
        "missing_keywords": list(missing)[:10],
        "readability": round(readability, 2)
    }


# ------------------------------
# TEXT CLEANING
# ------------------------------
def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    return text