import pdfplumber

def extract_text_from_resume(file_path):
    text=""

    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            page_text=page.extract_text()

            if page_text:
                text +=page_text+"\n"
    return text

skills_database=[
    "python",
    "java",
    "sql",
    "machine learning",
    "deep learning",
    "tensorflow",
    "keras",
    "numpy",
    "pandas",
    "opencv",
    "nlp",
    "cnn",
    "rnn",
    "lstm",
    "flask",
    "streamlit",
    "mongodb",
    "spring boot",
    "dsa"

]

def extract_skills(text):

    text = text.lower()

    found_skills = []

    for skill in skills_database:
        if skill in text:
            found_skills.append(skill)

    return found_skills