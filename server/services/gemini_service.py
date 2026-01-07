import os
from google import genai
from google.genai import types
from utils.prompts import ANALYZE_FOOD_PROMPT, ANALYZE_SUPPLEMENTS_PROMPT, BASE_PROMPT
from typing import Optional

model = "gemini-2.5-flash"


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


def analyze_ingredients(
    data: str,
    prompt: str = BASE_PROMPT,
    model: str = model,
    preferences: Optional[dict] = None,
) -> str:
    built_prompt = build_prompt(ANALYZE_FOOD_PROMPT, preferences)
    return generate_analysis_response(data, built_prompt, model)


def analyze_supplements(
    data: str,
    prompt: str = BASE_PROMPT,
    model: str = model,
    preferences: Optional[dict] = None,
) -> str:
    built_prompt = build_prompt(ANALYZE_SUPPLEMENTS_PROMPT, preferences)
    return generate_analysis_response(data, built_prompt, model)


def build_prompt(prompt: str, preferences: Optional[dict] = None) -> str:
    if not preferences:
        return prompt
    preference_str = "\n".join([f"- {key}: {value}" for key, value in preferences.items()])
    full_prompt = f"{prompt}\n\nUser Preferences:\n{preference_str}"
    print(f"Built Prompt: {full_prompt}")
    return full_prompt
