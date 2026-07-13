import streamlit as st

from modules.report_generator import generate_report
from modules.dashboard import show_dashboard
from modules.skill_dashboard import show_skill_dashboard
from modules.skill_gap import show_skill_gap
from modules.feedback_generator import generate_feedback
from modules.roadmap import generate_roadmap
from modules.career_recommender import recommend_career


def show_report():

    """
    Displays the complete interview report.
    """

    st.balloons()

    st.success("🎉 Interview Completed Successfully!")

    st.markdown("# 📊 AI Interview Report")

    st.caption(
        "Complete performance analysis generated using AI."
    )

    total_score = 0
    total_voice = 0
    total_stress = 0

    results = st.session_state.results

    if len(results) == 0:

        st.warning("No interview data available.")

        if st.button(
            "🔄 Restart Interview",
            use_container_width=True
        ):

            st.session_state.question_index = 0
            st.session_state.results = []
            st.session_state.questions = []
            st.session_state.start_interview = False

            st.rerun()

        return

    # ======================================
    # QUESTION WISE REPORT
    # ======================================

    st.subheader("📋 Question Wise Report")

    for i, result in enumerate(results):

        with st.expander(
            f"Question {i+1}"
        ):

            st.markdown("### ❓ Question")

            st.info(
                result["question"]
            )

            st.markdown("### 💬 Answer")

            st.write(
                result["answer"]
            )

            c1, c2 = st.columns(2)

            with c1:

                st.metric(
                    "Technical",
                    f"{result['score']:.1f}"
                )

                st.metric(
                    "Emotion",
                    result["emotion"]
                )

                st.metric(
                    "Stress",
                    f"{result['stress']}%"
                )

            with c2:

                st.metric(
                    "Voice",
                    f"{result['voice_score']:.1f}"
                )

                st.metric(
                    "Confidence",
                    f"{result['emotion_confidence']:.1f}%"
                )

                st.metric(
                    "Fillers",
                    len(result["fillers"])
                    if isinstance(
                        result["fillers"],
                        list
                    )
                    else result["fillers"]
                )

        total_score += result["score"]

        total_voice += result["voice_score"]

        total_stress += result["stress"]

    result_count = len(results)

    avg_score = total_score / result_count

    avg_voice = total_voice / result_count

    avg_stress = total_stress / result_count

    final_score = (

        avg_score * 0.60

        + avg_voice * 0.20

        + (100 - avg_stress) * 0.20

    )

    feedback = generate_feedback(

        avg_score,

        avg_voice,

        avg_stress,

        final_score

    )

    pdf_path = generate_report(

        results,

        final_score

    )
        # ======================================
    # OVERALL PERFORMANCE
    # ======================================

    st.divider()

    st.markdown("# 📊 Overall Performance")

    st.caption(
        "Summary of your interview performance."
    )

    c1, c2, c3, c4 = st.columns(4)

    c1.metric(
        "🎯 Technical",
        f"{avg_score:.1f}"
    )

    c2.metric(
        "🎤 Voice",
        f"{avg_voice:.1f}"
    )

    c3.metric(
        "😰 Stress",
        f"{avg_stress:.1f}%"
    )

    c4.metric(
        "🏆 Final Score",
        f"{final_score:.1f}"
    )

    st.progress(final_score / 100)

    st.caption(
        f"Overall Score : {final_score:.1f}/100"
    )

    # ======================================
    # PERFORMANCE LEVEL
    # ======================================

    if final_score >= 85:

        st.success(
            "⭐ Excellent Performance"
        )

    elif final_score >= 70:

        st.info(
            "👍 Good Performance"
        )

    elif final_score >= 50:

        st.warning(
            "⚠ Needs Improvement"
        )

    else:

        st.error(
            "❌ Poor Performance"
        )

    st.divider()

    # ======================================
    # DASHBOARD
    # ======================================

    st.markdown("# 📈 Performance Analytics")

    show_dashboard(

        avg_score,

        avg_voice,

        avg_stress,

        final_score

    )

    st.divider()

    # ======================================
    # SKILL ANALYSIS
    # ======================================

    st.markdown("# 🏆 Skill Analysis")

    show_skill_dashboard(

        results

    )

    st.divider()

    show_skill_gap(

        results

    )

    st.divider()

    # ======================================
    # CAREER RECOMMENDATION
    # ======================================

    st.markdown("# 🎯 Career Recommendation")

    recommend_career(

        results

    )

    st.divider()

    # ======================================
    # LEARNING ROADMAP
    # ======================================

    st.markdown("# 📚 Personalized Learning Roadmap")

    generate_roadmap(

        results

    )
    st.divider()

    # ======================================
    # AI FEEDBACK
    # ======================================

    st.markdown("# 🤖 AI Interview Feedback")

    st.caption(
        "Personalized feedback generated from your interview performance."
    )

    st.markdown("## 💪 Strengths")

    for strength in feedback["strengths"]:

        st.success(strength)

    st.markdown("## 📈 Areas for Improvement")

    for improvement in feedback["improvements"]:

        st.warning(improvement)

    st.markdown("## 🏆 Final Recommendation")

    st.info(
        feedback["recommendation"]
    )

    st.divider()

    # ======================================
    # DOWNLOAD REPORT
    # ======================================

    st.markdown("# 📄 Download Interview Report")

    st.caption(
        "Download your complete interview assessment report."
    )

    with open(pdf_path, "rb") as pdf:

        st.download_button(

            label="📄 Download PDF Report",

            data=pdf,

            file_name="AI_Interview_Report.pdf",

            mime="application/pdf",

            use_container_width=True

        )

    st.divider()

    # ======================================
    # START NEW INTERVIEW
    # ======================================

    if st.button(

        "🔄 Start New Interview",

        use_container_width=True

    ):

        st.session_state.question_index = 0

        st.session_state.results = []

        st.session_state.questions = []

        st.session_state.start_interview = False

        st.rerun()