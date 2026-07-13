def generate_feedback(technical,voice,stress,final):

    strengths=[]
    improvements=[]
#Technical
    if technical >=80:
        strengths.append("Strong technical knowledge")
    elif technical >=60:
        strengths.append("Good understanding of technical concepts.")
        improvements.append("Practice advanced technical questions.")
    else:
        improvements.append("Improve technical fundamentals.")
    
    #Voice
    if voice >= 80:
        strengths.append("Confident and clear communication.")
    elif voice >= 60:
        improvements.append("Improve confidence while speaking. ")
    else:
        improvements.append("Reduce filler words and speak more confidently.")

    #Stress
    if stress <=30:
        strengths.append("Remained calm during the interview .")
    elif stress <=60:
        improvements.append("Maintain a more relaxed posture .")
    else:
        improvements.append("Practice mock interviews to reduce stress.")

    
    #Final recomendation 
    if final >=85:
        recommendation="⭐ Highly Recommended"
    elif final >=70:
        recommendation="✅ Recommended"
    elif final >=50:
        recommendation="⚠ Consider after improvement"

    else:
        recommendation="❌ Not Recommended"
    
    return{
        "strengths":strengths,
        "improvements":improvements,
        "recommendation":recommendation
    }

    