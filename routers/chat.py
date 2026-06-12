from fastapi import APIRouter

from schemas.chat import (
    ChatRequest,
    ChatResponse
)

from services.emergency import (
    check_emergency
)

from services.safety import (
    check_safety
)

from services.medical_api import (
    get_medical_info
)

from services.medicine_api import (
    get_medicine_info
)

from services.llm import (
    ask_llm
)

router = APIRouter()


@router.post(
    "/chat",
    response_model=ChatResponse
)
async def chat(request: ChatRequest):

    question = request.question

    # Emergency Detection
    emergency_response = check_emergency(
        question
    )

    if emergency_response:

        return ChatResponse(
            success=True,
            source="emergency_detection",
            answer=emergency_response
        )

    # Safety Filter
    safety_response = check_safety(
        question
    )

    if safety_response:

        return ChatResponse(
            success=True,
            source="safety_filter",
            answer=safety_response
        )

    # Disease Information
    medical_response = get_medical_info(
        question
    )

    if medical_response:

        return ChatResponse(
            success=True,
            source="medlineplus_style",
            answer=medical_response
        )

    # Medicine Information
    medicine_response = get_medicine_info(
        question
    )

    if medicine_response:

        return ChatResponse(
            success=True,
            source="rxnorm",
            answer=medicine_response
        )

    # Gemini Fallback
    answer = ask_llm(
        question
    )

    return ChatResponse(
        success=True,
        source="gemini",
        answer=answer
    )