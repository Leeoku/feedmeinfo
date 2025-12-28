import os
from google import genai
from google.genai import types
from utils.prompts import ANALYZE_FOOD_PROMPT

model = "gemini-2.5-flash"
prompt = "Hello world"


def get_gemini_client():
    return genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


def analyze_ingredients_response(data: str, prompt: str = prompt, model: str = model) -> str:
    client = get_gemini_client()
    response = client.models.generate_content(
        model=model,
        contents=data,
        config=types.GenerateContentConfig(
            system_instruction=ANALYZE_FOOD_PROMPT
        ),
    )
    print(response.text)
    return response.text
