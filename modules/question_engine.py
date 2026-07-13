questions = [
    "tell me about yourself",
    "what is machine learning ?",
    "explain the difference between ai and machine learning",
    "what are the four pillars of oop ?",
    "explain overfitting in machine learning"
]
easy_questions=[
    "what is python?",
    "what is oop ?",
    "what is machine learning ?"
]
medium_questions=[
    "explain overfitting",
    "differnce between ai and machine learning"
]
hard_questions=[
    "explain bias-variance tradeoff",
    "what is gradient descent ?"
]
skill_questions = {
    "python": [
        "What are decorators in Python?",
        "Difference between list and tuple?"
    ],

    "java": [
        "Explain JVM and JDK.",
        "What is method overloading?"
    ],

    "sql": [
        "Difference between WHERE and HAVING?",
        "What is normalization?"
    ],

    "machine learning": [
        "Explain overfitting.",
        "What is bias variance tradeoff?"
    ],

    "deep learning": [
        "What is backpropagation?",
        "What is an activation function?"
    ],

    "tensorflow": [
        "What is TensorFlow?",
        "Difference between TensorFlow and PyTorch?"
    ],

    "keras": [
        "What is Sequential API?",
        "Difference between Keras and TensorFlow?"
    ],

    "cnn": [
        "Explain convolution layer.",
        "What is pooling?"
    ]
}
def generate_questions(skills):

    questions = []

    for skill in skills:
        if skill in skill_questions:
            questions.extend(skill_questions[skill])

    return questions[:10]
# def get_question(index):
#     if index < len(questions):
#         return questions[index]
#     return None

def get_next_question(score, stress):

    if score >= 75 and stress <= 40:
        if len(hard_questions) > 0:
            return hard_questions.pop(0)

    elif score < 50 or stress > 70:
        if len(easy_questions) > 0:
            return easy_questions.pop(0)

    else:
        if len(medium_questions) > 0:
            return medium_questions.pop(0)

    return None