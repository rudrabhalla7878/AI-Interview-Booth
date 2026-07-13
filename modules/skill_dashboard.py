import streamlit as st
import matplotlib.pyplot as plt 
def show_skill_dashboard(results):

    skill_scores = {}

    # ---------------- Collect Scores ---------------- #

    for result in results:

        skill = result.get("skill", "Unknown")
        score = result.get("score", 0)

        if skill not in skill_scores:
            skill_scores[skill] = []

        skill_scores[skill].append(score)

    if len(skill_scores) == 0:
        return

    # ---------------- Average ---------------- #

    average_scores = {}

    for skill in skill_scores:

        average_scores[skill] = (
            sum(skill_scores[skill]) /
            len(skill_scores[skill])
        )

    # ---------------- Heading ---------------- #

    st.divider()

    st.subheader("📊 Skill Performance")

    # ---------------- Chart ---------------- #

    skills = list(average_scores.keys())
    scores = list(average_scores.values())

    fig, ax = plt.subplots(figsize=(8, 4))

    ax.barh(skills, scores)

    ax.set_xlim(0, 100)

    ax.set_xlabel("Score")

    ax.set_title("Skill-wise Performance")

    st.pyplot(fig)

    # ---------------- Strongest ---------------- #

    strongest = max(
        average_scores,
        key=average_scores.get
    )

    weakest = min(
        average_scores,
        key=average_scores.get
    )

    col1, col2 = st.columns(2)

    with col1:

        st.success(
            f"🏆 Strongest Skill\n\n"
            f"{strongest} ({average_scores[strongest]:.2f})"
        )

    with col2:

        st.warning(
            f"📚 Needs Improvement\n\n"
            f"{weakest} ({average_scores[weakest]:.2f})"
        )

    # ---------------- Table ---------------- #

    st.subheader("Skill Scores")

    for skill in average_scores:

        st.progress(
            average_scores[skill] / 100
        )

        st.write(
            f"**{skill}** : {average_scores[skill]:.2f}%"
        )