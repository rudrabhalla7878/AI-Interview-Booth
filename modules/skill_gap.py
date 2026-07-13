import streamlit as st


def show_skill_gap(results):

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

    # ---------------- Average Score ---------------- #

    average_scores = {}

    for skill in skill_scores:

        average_scores[skill] = (
            sum(skill_scores[skill]) /
            len(skill_scores[skill])
        )

    strong_skills = []
    weak_skills = []

    for skill, score in average_scores.items():

        if score >= 75:
            strong_skills.append((skill, score))

        else:
            weak_skills.append((skill, score))

    st.divider()

    st.subheader("📊 Skill Gap Analysis")

    col1, col2 = st.columns(2)

    # ---------------- Strong Skills ---------------- #

    with col1:

        st.success("🏆 Strong Skills")

        if len(strong_skills) == 0:

            st.info("No strong skills detected yet.")

        else:

            for skill, score in sorted(
                strong_skills,
                key=lambda x: x[1],
                reverse=True
            ):

                st.write(
                    f"✅ **{skill}** ({score:.2f}%)"
                )

    # ---------------- Weak Skills ---------------- #

    with col2:

        st.warning("📚 Needs Improvement")

        if len(weak_skills) == 0:

            st.success("Excellent! No weak skills detected.")

        else:

            for skill, score in sorted(
                weak_skills,
                key=lambda x: x[1]
            ):

                st.write(
                    f"🔸 **{skill}** ({score:.2f}%)"
                )