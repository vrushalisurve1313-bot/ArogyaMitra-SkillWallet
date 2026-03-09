from fastapi import APIRouter
from services.ai_service import analyze_symptoms

router = APIRouter()

@router.post("/analyze-symptoms")
def analyze(data: dict):

    symptoms = data.get("symptoms")

    result = analyze_symptoms(symptoms)

    return {"analysis": result}