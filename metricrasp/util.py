import json


def json_parser(json_file_path):
    try:
        with open(json_file_path) as json_file:
            json_data = json.load(json_file)
    except:
        raise "The conf file does not exist"

    return json_data