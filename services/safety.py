FORBIDDEN_KEYWORDS = [

    "dosage",
    "dose",
    "how much",
    "prescribe",
    "prescription",
    "should i take",
    "can i take",
    "diagnose",
    "do i have",
    "treatment"

]

def check_safety(question: str):

    question = question.lower()

    for keyword in FORBIDDEN_KEYWORDS:

        if keyword in question:

            return (
                "I cannot provide diagnosis, "
                "medicine dosage, prescriptions, "
                "or treatment advice. "
                "Please consult a licensed "
                "healthcare professional."
            )

    return None