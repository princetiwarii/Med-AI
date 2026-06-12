import os
from dotenv import load_dotenv
from google import genai

# Load environment variables from .env
load_dotenv()

# Create Gemini client
client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def ask_llm(question: str):

    prompt = f"""
    You are an AI Medical Information Chatbot.

    Provide:

    • General health information
    • Disease explanations
    • Prevention tips
    • Medicine usage information

    Do NOT:

    • Diagnose diseases
    • Prescribe medications
    • Recommend dosages
    • Recommend treatment decisions

    Always suggest consulting
    a licensed healthcare professional.

    Question:
    {question}
    """

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        return response.text

    except Exception:

        return (
        "The AI service is temporarily unavailable "
        "due to high demand. Please try again "
        "after a few minutes."
        )