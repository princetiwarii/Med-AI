import requests


MEDICINES = [
    "paracetamol",
    "ibuprofen",
    "aspirin",
    "acetaminophen"
]


def get_medicine_info(question: str):

    question = question.lower()

    medicine_found = None

    for medicine in MEDICINES:

        if medicine in question:
            medicine_found = medicine
            break

    if not medicine_found:
        return None

    try:

        url = (
            f"https://rxnav.nlm.nih.gov/REST/drugs.json"
            f"?name={medicine_found}"
        )

        response = requests.get(url)

        if response.status_code != 200:
            return None

        data = response.json()

        group = data.get("drugGroup", {})

        concept_group = group.get("conceptGroup", [])

        if concept_group:

            return (
                f"Medicine: {medicine_found.title()}\n\n"
                f"RxNorm successfully identified this medicine.\n\n"
                "For detailed usage instructions, "
                "consult a healthcare professional "
                "or pharmacist.\n\n"
                "This chatbot does not provide "
                "dosage recommendations."
            )

        return None

    except Exception:

        return (
            "Unable to retrieve medicine information "
            "at this time."
        )