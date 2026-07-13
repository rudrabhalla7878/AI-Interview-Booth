def analyze_voice(answer):

    filler_words=[
        "um","uh","like","actually",
        "basically","you know","hmm"
    ]
    words=answer.lower().split()
    filler_count=0

    for word in words:
        if word in filler_words:
            filler_count += 1

    total_words=len(words)
    if total_words ==0:
        confidence_score=0
    else:
        filler_ratio=filler_count/total_words
        confidence_score=max(
            0,
            100 - (filler_ratio * 100)
        )
        if total_words <5:
            confidence_score -=20
            confidence_score=max(0,confidence_score)
    return round(confidence_score,2),filler_count