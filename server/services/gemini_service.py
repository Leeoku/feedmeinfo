import os
from google import genai
from google.genai import types
from utils.prompts import ANALYZE_FOOD_PROMPT, ANALYZE_SUPPLEMENTS_PROMPT

model = "gemini-2.5-flash"
prompt = "Hello world"


def get_gemini_client():
    return genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def generate_analysis_response(data: str, system_prompt: str, model: str = model) -> str:
    client = get_gemini_client()
    response = client.models.generate_content(
        model=model,
        contents=data,
        config=types.GenerateContentConfig(system_instruction=system_prompt),
    )
    print(response.text)
    return response.text


def analyze_ingredients(data: str, prompt: str = prompt, model: str = model) -> str:
    return generate_analysis_response(data, ANALYZE_FOOD_PROMPT, model)


def analyze_supplements(data: str, prompt: str = prompt, model: str = model) -> str:
    return generate_analysis_response(data, ANALYZE_SUPPLEMENTS_PROMPT, model)
