import json


def json_parser(json_file_path: str) -> dict:
    try:
        with open(json_file_path) as json_file:
            json_data: dict = json.load(json_file)
    except:
        raise "The conf file does not exist"

    return json_data