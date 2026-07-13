from modules.resume_parser import *

text = extract_text_from_resume("resume.pdf")

skills = extract_skills(text)

print(skills)