EMERGENCY_KEYWORDS = [

    "chest pain",
    "breathing difficulty",
    "shortness of breath",
    "heavy bleeding",
    "unconscious",
    "stroke",
    "allergic reaction"

]


def check_emergency(question: str):

    question = question.lower()

    for keyword in EMERGENCY_KEYWORDS:

        if keyword in question:

            return (
                "⚠️ This may be a serious "
                "medical condition. "
                "Please contact a doctor "
                "or emergency medical "
                "service immediately."
            )

    return None