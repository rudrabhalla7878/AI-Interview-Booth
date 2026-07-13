from modules.voice_analysis import analyze_voice

answer = """
Machine learning is basically a branch of AI
that actually learns from data.
"""

score, fillers = analyze_voice(answer)

print("Confidence Score:", score)
print("Filler Words:", fillers)