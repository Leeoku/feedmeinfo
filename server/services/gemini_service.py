import os
from google import genai

model = "gemini-2.5-flash"
prompt = "Explain how AI works in a few words"


def get_gemini_client():
    return genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


def generate_response(prompt: str = prompt, model: str = model) -> str:
    client = get_gemini_client()
    response = client.models.generate_content(
        model=model, contents=prompt
    )
    print(response.text)
    return response.text
