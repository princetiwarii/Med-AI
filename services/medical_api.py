from services.llm import ask_llm


COMMON_DISEASES = [
    "diabetes",
    "dengue",
    "malaria",
    "asthma",
    "fever",
    "migraine",
    "cold",
    "cough",
    "high blood pressure",
    "hypertension"
]


def get_medical_info(question: str):

    question_lower = question.lower()

    for disease in COMMON_DISEASES:

        if disease in question_lower:

            prompt = f"""
Provide patient-friendly health information
similar to MedlinePlus.

Disease: {disease}

Include:

- Definition
- Common Symptoms
- Prevention Tips
- When to consult a doctor

Do NOT diagnose.
Do NOT recommend medications.
"""

            return ask_llm(prompt)

    return None