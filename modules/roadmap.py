import streamlit as st


def generate_roadmap(results):

    skill_scores = {}

    # ---------------- Collect Scores ---------------- #

    for result in results:

        skill = result.get("skill", "Unknown")
        score = result.get("score", 0)

        if skill not in skill_scores:
            skill_scores[skill] = []

        skill_scores[skill].append(score)

    average_scores = {}

    for skill in skill_scores:

        average_scores[skill] = (
            sum(skill_scores[skill]) /
            len(skill_scores[skill])
        )

    roadmap = {}

    for skill, score in average_scores.items():

        if score >= 75:
            continue

        if skill == "Python":

            roadmap[skill] = [
                "Revise Functions",
                "Practice OOP",
                "Solve 20 Python Problems"
            ]

        elif skill == "Java":

            roadmap[skill] = [
                "Learn OOP Concepts",
                "Collections Framework",
                "Exception Handling"
            ]

        elif skill == "Machine Learning":

            roadmap[skill] = [
                "Linear Regression",
                "Overfitting & Underfitting",
                "Model Evaluation"
            ]

        elif skill == "DBMS":

            roadmap[skill] = [
                "Normalization",
                "SQL Joins",
                "Transactions"
            ]

        elif skill == "Algorithms":

            roadmap[skill] = [
                "Big O Analysis",
                "Binary Search",
                "Sorting Algorithms"
            ]

        elif skill == "Data Structures":

            roadmap[skill] = [
                "Linked List",
                "Stack & Queue",
                "Trees"
            ]

        elif skill == "Operating Systems":

            roadmap[skill] = [
                "Deadlock",
                "Scheduling",
                "Memory Management"
            ]

    st.divider()

    st.subheader("📚 Personalized Learning Roadmap")

    if len(roadmap) == 0:

        st.success(
            "Excellent! No major weak skills detected."
        )

        return

    week = 1

    for skill, topics in roadmap.items():

        st.markdown(f"### Week {week} - {skill}")

        for topic in topics:

            st.write(f"✅ {topic}")

        week += 1