import json
from typing import TypedDict

# in ocr.space, the parsed text is data["ParsedResults"][0]["ParsedText"]
def parse_json_file(file_path: str) -> dict[str, Any]:
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data
