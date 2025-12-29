from utils.helpers import parse_json_file 
from dotenv import load_dotenv
from services.gemini_service import analyze_ingredients

def main():
    load_dotenv()

    # For now choose OCR + LLM instead of multimodal LLM
    data = parse_json_file('data/v1.json')
    parsed_data = data["ParsedResults"][0]["ParsedText"]
    print(parsed_data)
    # analyze_ingredients(parsed_data)


if __name__ == "__main__":
    main()
