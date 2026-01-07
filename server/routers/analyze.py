from fastapi import APIRouter, UploadFile, File
from pathlib import Path
from utils.helpers import parse_json_file
from services.gemini_service import analyze_ingredients

router = APIRouter()


@router.get("/")
async def root():
    return {"message": "Hello World"}


@router.post("/analyze")
async def analyze_food():
    ocr_data = parse_json_file("data/v1.json")
    parsed_text = ocr_data["ParsedResults"][0]["ParsedText"]
    analysis = analyze_ingredients(parsed_text, preferences={"nutrition": ["low sugar", "high protein"]})

    return {"ocr_text": parsed_text, "gemini_analysis": analysis}
