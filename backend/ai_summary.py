import random

def generate_summary(data):

    name = data.get('name', 'Candidate')
    skills = data.get('skills', '')
    experience = data.get('experience', '')
    education = data.get('education', '')

    templates = [
        f"{name} is a results-driven professional with strong expertise in {skills}. "
        f"Bringing hands-on experience in {experience}, {name} demonstrates strong problem-solving abilities "
        f"and a commitment to delivering high-quality solutions. Holds academic background in {education}.",

        f"Highly motivated and detail-oriented professional skilled in {skills}. "
        f"With experience in {experience}, {name} has consistently delivered efficient and scalable solutions. "
        f"Educational foundation in {education} supports strong analytical and technical capabilities.",

        f"Dynamic and performance-focused individual with expertise in {skills}. "
        f"Experienced in {experience}, {name} excels at building impactful solutions and driving business results. "
        f"Academic qualifications in {education} complement technical proficiency."
    ]

    return random.choice(templates)