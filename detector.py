from scam_keywords import SCAM_KEYWORDS
def detect_scam(text):
        found=[]
        score=0
        text=text.lower()
        for keyword in SCAM_KEYWORDS:
            if keyword in text:
                score+=20
                found.append(keyword)
        if score>=60:
             risk="High Risk! "
        elif score>=30:
             risk="Suspicious!"
        else:
             risk="Safe!"
        return risk,score,found