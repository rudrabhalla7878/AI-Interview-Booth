emotion_scores = {
    "happy": 90,
    "neutral": 75,
    "surprise": 80,
    "sad": 40,
    "fear": 35,
    "angry": 30,
    "disgust": 20
}

def get_emotion_score(emotion):
    return emotion_scores.get(emotion, 50)