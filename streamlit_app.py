import streamlit as st
import tempfile
import sys


st.write(sys.version)

from modules.resume_parser import extract_text_from_resume
#from modules.question_generator import generate_questions
#from modules.interview import run_interview

# ---------------------------------------------
# PAGE CONFIG
# ---------------------------------------------

st.set_page_config(
    page_title="AI Interview Booth",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)
def load_css():

    with open("assets/style.css") as f:

        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )

load_css()

# ---------------------------------------------
# CUSTOM CSS
# ---------------------------------------------

st.markdown("""
<style>

.main{
    background:#f7f9fc;
}

.block-container{
    padding-top:2rem;
}

.title{
    text-align:center;
    font-size:48px;
    font-weight:700;
    color:#2563eb;
}

.subtitle{
    text-align:center;
    color:gray;
    font-size:18px;
    margin-bottom:25px;
}

.skill{
    display:inline-block;
    background:#2563eb;
    color:white;
    padding:7px 15px;
    margin:5px;
    border-radius:25px;
    font-size:14px;
}

.summary-box{
    background:white;
    padding:18px;
    border-radius:12px;
    border:1px solid #dddddd;
    margin-bottom:15px;
}

</style>
""", unsafe_allow_html=True)

# ---------------------------------------------
# HEADER
# ---------------------------------------------

# ---------------------------------------------
# HEADER
# ---------------------------------------------

st.markdown("""
<div style='text-align:center;padding:20px;'>

<h1 style='color:#2563EB;font-size:50px;margin-bottom:5px;'>
🤖 AI Interview Booth
</h1>

<h3 style='color:gray;font-weight:400;'>
AI Powered Resume Assessment & Career Evaluation Platform
</h3>

<p style='font-size:18px;color:#555;'>
Upload your resume, take an AI-powered interview,
analyze your performance, identify skill gaps,
and receive a personalized learning roadmap.
</p>

</div>
""", unsafe_allow_html=True)

# ---------------------------------------------
# SIDEBAR
# ---------------------------------------------

with st.sidebar:

    st.image(
        "https://img.icons8.com/fluency/96/artificial-intelligence.png",
        width=80
    )

    st.title("AI Interview Booth")

    st.write("### Modules")

    st.success("Resume Parsing")
    st.success("Question Generation")
    st.success("Speech Recognition")
    st.success("Emotion Detection")
    st.success("Voice Analysis")
    st.success("Stress Detection")
    st.success("Career Recommendation")

    st.divider()

    st.info(
        "Developed using Python, Streamlit and AI."
    )

# ---------------------------------------------
# UPLOAD
# ---------------------------------------------

# ---------------------------------------------
# HERO METRICS
# ---------------------------------------------

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.metric("📄 Resume Parser", "AI")

with c2:
    st.metric("🎤 Interview", "Live")

with c3:
    st.metric("📊 Analytics", "Enabled")

with c4:
    st.metric("🤖 AI Feedback", "Ready")

st.divider()

# ---------------------------------------------
# UPLOAD
# ---------------------------------------------

st.markdown("## 📄 Upload Your Resume")

st.info(
    """
    **Instructions**

    • Upload your latest resume in PDF format.

    • AI extracts your skills automatically.

    • Personalized interview questions are generated.

    • AI evaluates your interview performance.
    """
)

resume = st.file_uploader(
    "Choose Resume",
    type=["pdf"],
    help="Upload PDF Resume"
)
# ---------------------------------------------
# RESUME PROCESSING
# ---------------------------------------------

if resume:

    with tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".pdf"
    ) as tmp:

        tmp.write(resume.read())
        resume_path = tmp.name

    st.success("✅ Resume uploaded successfully!")

    resume_text = extract_text_from_resume(
        resume_path
    )

    # ---------------------------------------------
    # SKILL LIST
    # ---------------------------------------------

    skills = [

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
        "cnn",
        "streamlit",
        "scikit-learn",
        "oop",
        "object-oriented programming",
        "data structures",
        "algorithms",
        "dbms",
        "operating systems"

    ]

    detected_skills = []

    resume_lower = resume_text.lower()

    for skill in skills:

        if skill in resume_lower:

            detected_skills.append(skill.title())

    # ---------------------------------------------
    # GENERATE QUESTIONS
    # ---------------------------------------------

    if "questions" not in st.session_state:

        st.session_state.questions = generate_questions(
            detected_skills
        )

    if "question_index" not in st.session_state:

        st.session_state.question_index = 0

    if "results" not in st.session_state:

        st.session_state.results = []

    if "start_interview" not in st.session_state:

        st.session_state.start_interview = False

    # ---------------------------------------------
    # CANDIDATE SUMMARY
    # ---------------------------------------------

    st.markdown("## 👤 Candidate Summary")

    c1, c2, c3 = st.columns(3)

    with c1:

        st.metric(
            "Skills",
            len(detected_skills)
        )

    with c2:

        st.metric(
            "Questions",
            len(st.session_state.questions)
        )

    with c3:

        st.metric(
            "Status",
            "Ready"
        )

    st.divider()

    # ---------------------------------------------
    # SKILL CHIPS
    # ---------------------------------------------

    st.markdown("## 🏷️ Detected Skills")

    if len(detected_skills) == 0:

        st.warning(
            "No predefined skills detected in the resume."
        )

    else:

        html = ""

        for skill in detected_skills:

            html += (
                f"<span class='skill'>{skill}</span>"
            )

        st.markdown(
            html,
            unsafe_allow_html=True
        )

    st.divider()

    # ---------------------------------------------
    # RESUME PREVIEW
    # ---------------------------------------------

    with st.expander(
        "📄 Resume Preview",
        expanded=False
    ):

        st.text_area(

            "",

            resume_text,

            height=300

        )

    st.divider()

    # ---------------------------------------------
    # START INTERVIEW
    # ---------------------------------------------

    if not st.session_state.start_interview:

        st.markdown(
            "## 🎤 Ready to Begin?"
        )

        st.write(
            "Click the button below to start your AI interview."
        )

        if st.button(

            "🚀 Start Interview",

            use_container_width=True,
            type="primary"

        ):

            st.session_state.start_interview = True

            st.rerun()

    # ---------------------------------------------
    # RUN INTERVIEW
    # ---------------------------------------------

    if st.session_state.start_interview:

        run_interview(
            st.session_state.questions
        )