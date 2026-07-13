import random


def generate_questions(skills):

    questions = []

    if "python" in skills:

        questions.append({
            "skill": "Python",
            "question": "What is Python?"
        })

        questions.append({
            "skill": "Python",
            "question": "Difference between List and Tuple?"
        })

    if "java" in skills:

        questions.append({
            "skill": "Java",
            "question": "Explain OOP concepts."
        })

        questions.append({
            "skill": "Java",
            "question": "Difference between abstract class and interface?"
        })

    if "machine learning" in skills:

        questions.append({
            "skill": "Machine Learning",
            "question": "What is overfitting?"
        })

        questions.append({
            "skill": "Machine Learning",
            "question": "Difference between AI and Machine Learning?"
        })

    if "tensorflow" in skills:

        questions.append({
            "skill": "TensorFlow",
            "question": "What is TensorFlow used for?"
        })

    if "cnn" in skills:

        questions.append({
            "skill": "CNN",
            "question": "Explain the architecture of CNN."
        })

    if "dbms" in skills:

        questions.append({
            "skill": "DBMS",
            "question": "What is normalization?"
        })

        questions.append({
            "skill": "DBMS",
            "question": "Difference between DELETE, DROP and TRUNCATE?"
        })

    if "operating systems" in skills:

        questions.append({
            "skill": "Operating Systems",
            "question": "What is a deadlock?"
        })

        questions.append({
            "skill": "Operating Systems",
            "question": "Explain process and thread."
        })

    if "data structures" in skills:

        questions.append({
            "skill": "Data Structures",
            "question": "Difference between Stack and Queue?"
        })

        questions.append({
            "skill": "Data Structures",
            "question": "Explain Linked List."
        })

    if "algorithms" in skills:

        questions.append({
            "skill": "Algorithms",
            "question": "What is time complexity?"
        })

        questions.append({
            "skill": "Algorithms",
            "question": "Explain Big O notation."
        })

    random.shuffle(questions)

    return questions