from modules.question_engine import get_next_question
from modules.evaluator import evaluate
from modules.stress_analysis import detect_stress
from modules.audio import get_audio_input
from modules.face_analysis import detect_emotion
from modules.voice_analysis import analyze_voice

responses = {}
scores = []
stress_levels = []
emotion_levels = []
voice_scores=[]


# Initial values
score = 0
stress = 0

while True:

    question = get_next_question(score, stress)

    if question is None:
        break

    print("\n===================================")
    print("Interview Question:")
    print(question)

    # Candidate answer
    answer = get_audio_input()
    if len(answer.split()) <3:
        print("Answer too short .Please answer again..")
        continue
    confidence_score, filler_count = analyze_voice(answer)

    voice_scores.append(confidence_score)

    print(f"Voice Confidence: {confidence_score}/100")
    print(f"Filler Words: {filler_count}")

    responses[question] = answer

    # Evaluate answer quality
    score = evaluate(question, answer)
    scores.append(score)

    # Stress analysis
    stress = detect_stress()
    stress_levels.append(stress)

    # Emotion analysis
    emotion = detect_emotion()
    emotion_levels.append(emotion)

    print("\nScore:", score, "/100")
    print("Stress Level:", stress, "%")
    print("Detected Emotion:", emotion)

    if stress > 70:
        print("Candidate under stress.")
        print("Switching to easier questions.")
    elif score >= 75 and stress <= 40:
        print("Candidate performing well.")
        print("Increasing difficulty level.")

# -------------------------
# FINAL REPORT
# -------------------------

average_score = sum(scores) / len(scores) if scores else 0
average_stress = sum(stress_levels) / len(stress_levels) if stress_levels else 0


average_voice_score = (
    sum(voice_scores) / len(voice_scores)
    if voice_scores else 0
)

print(f"Average Interview Score: {average_score:.2f}/100")
print(f"Average Stress Level: {average_stress:.2f}%")
# print(f"Average Emotion Score: {average_emotion_score:.2f}/100")
print(f"Average Voice Confidence: {average_voice_score:.2f}/100")

emotion_score_map = {
    "happy": 90,
    "neutral": 75,
    "surprise": 85,
    "sad": 40,
    "fear": 35,
    "angry": 30,
    "disgust": 20
}

emotion_scores = [
    emotion_score_map.get(e.lower(), 50)
    for e in emotion_levels
]

average_emotion_score = (
    sum(emotion_scores) / len(emotion_scores)
    if emotion_scores else 50
)

final_score = (
    average_score * 0.5 +
    average_emotion_score * 0.20 +
    average_voice_score *0.15+
    (100 - average_stress) * 0.15
)

print("\n========== FINAL REPORT ==========")

print(f"Average Interview Score: {average_score:.2f}/100")
print(f"Average Stress Level: {average_stress:.2f}%")
print(f"Average Emotion Score: {average_emotion_score:.2f}/100")
print(f"Average Voice Confidence: {average_voice_score:.2f}/100")
print(f"Final Interview Score: {final_score:.2f}/100")

print("\n====== INTERVIEW RESPONSES ======")

for question, answer in responses.items():
    print("\nQuestion:", question)
    print("Answer:", answer)

print("\nEmotion History:", emotion_levels)

print("\n========== INTERVIEW COMPLETED ==========")