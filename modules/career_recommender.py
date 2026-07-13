import streamlit as st


def recommend_career(results):

    skills = {}

    for result in results:

        skill = result.get("skill", "Unknown")
        score = result.get("score", 0)

        if skill not in skills:
            skills[skill] = []

        skills[skill].append(score)

    avg = {}

    for skill in skills:
        avg[skill] = sum(skills[skill]) / len(skills[skill])

    recommendations = []

    # ML Engineer
    if (
        avg.get("Machine Learning", 0) >= 70 and
        avg.get("Python", 0) >= 70
    ):
        recommendations.append(
            ("⭐⭐⭐⭐⭐", "Machine Learning Engineer")
        )

    # AI Engineer
    if (
        avg.get("Machine Learning", 0) >= 70 and
        avg.get("CNN", 0) >= 60
    ):
        recommendations.append(
            ("⭐⭐⭐⭐", "AI Engineer")
        )

    # Backend Developer
    if (
        avg.get("Python", 0) >= 70 or
        avg.get("Java", 0) >= 70
    ):
        recommendations.append(
            ("⭐⭐⭐⭐", "Backend Developer")
        )

    # Data Analyst
    if (
        avg.get("Python", 0) >= 60 and
        avg.get("DBMS", 0) >= 60
    ):
        recommendations.append(
            ("⭐⭐⭐", "Data Analyst")
        )

    # Software Engineer
    if (
        avg.get("Algorithms", 0) >= 60 and
        avg.get("Data Structures", 0) >= 60
    ):
        recommendations.append(
            ("⭐⭐⭐", "Software Engineer")
        )

    st.divider()

    st.subheader("🎯 Recommended Career Paths")

    if len(recommendations) == 0:

        st.warning(
            "No strong recommendation yet. Improve technical skills."
        )

    else:

        for stars, role in recommendations:

            st.success(f"{stars}  {role}")

    return recommendations