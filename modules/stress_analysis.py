# import random
from modules.face_analysis import detect_emotion

def detect_stress(emotion):
   

   stress_mapping={
      "happy":20,
      "neutral":40,
      "surprise":45,
      "sad":70,
      "fear":85,
      "angry":90,
      "disgust":80
   }

   stress=stress_mapping.get(emotion,50)

   print("Detected Emotion:",emotion)

   return stress