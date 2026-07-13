from sentence_transformers import SentenceTransformer, util

# Load model once
model = SentenceTransformer("all-MiniLM-L6-v2")

ideal_answers = {
    "what is python?":
        "Python is a high-level interpreted programming language used for software development, data science, machine learning and automation.",

    "what is oop ?":
        "Object Oriented Programming is a programming paradigm based on objects and classes. The four pillars are encapsulation, inheritance, polymorphism and abstraction.",

    "what is machine learning ?":
        "Machine learning is a branch of artificial intelligence that enables systems to learn from data and improve performance without explicit programming.",

    "explain overfitting":
        "Overfitting occurs when a machine learning model learns training data too well including noise and performs poorly on unseen data.",

    "difference between ai and machine learning":
        "Artificial Intelligence is the broader field of creating intelligent systems while Machine Learning is a subset of AI that learns from data.",

    "explain bias variance tradeoff":
        "Bias variance tradeoff balances underfitting and overfitting to achieve good generalization performance.",

    "what is gradient descent ?":
        "Gradient descent is an optimization algorithm used to minimize the loss function by updating parameters in the opposite direction of the gradient."
}


def evaluate(question, answer):

    question = question.strip().lower()
    answer = answer.strip()

    ideal_answer = ideal_answers.get(question)

    if ideal_answer is None:
        return 50

    answer_embedding = model.encode(answer, convert_to_tensor=True)
    ideal_embedding = model.encode(ideal_answer, convert_to_tensor=True)

    similarity = util.cos_sim(
        answer_embedding,
        ideal_embedding
    ).item()

    score = similarity * 100

    score = max(0, (similarity - 0.30) * 140)
    score = min(score, 100)

    return round(score, 2)