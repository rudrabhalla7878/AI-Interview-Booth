from deepface import DeepFace
import cv2
import time
from collections import Counter

def detect_emotion():

    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        return "neutral", 0

    time.sleep(2)

    emotions = []
    confidence_scores = []

    for i in range(10):

        ret, frame = cap.read()

        if not ret:
            continue

        try:

            result = DeepFace.analyze(
                img_path=frame,
                actions=["emotion"],
                detector_backend="opencv",
                enforce_detection=False
            )

            emotion = result[0]["dominant_emotion"]
            confidence = result[0]["emotion"][emotion]

            emotions.append(emotion)
            confidence_scores.append(confidence)

        except Exception as e:
            print(e)

    cap.release()

    if len(emotions) == 0:
        return "neutral", 0

    final_emotion = Counter(emotions).most_common(1)[0][0]

    total = 0
    count = 0

    for i in range(len(emotions)):
        if emotions[i] == final_emotion:
            total += confidence_scores[i]
            count += 1

    avg_confidence = total / count

    return final_emotion, round(avg_confidence, 2)