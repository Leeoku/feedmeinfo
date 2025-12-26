from utils.helpers import parse_json_file 


def main():
    data = parse_json_file('data/v1.json')
    parsed_data = data["ParsedResults"][0]["ParsedText"]
    print(data)


if __name__ == "__main__":
    main()
