import json


def get_transactions(path_to_json: str) -> list:
    """return a list of all transactions"""
    try:
        with open(path_to_json, "r", encoding="utf-8") as f:
            data = json.load(f)

            if not isinstance(data, list):
                raise ValueError("json file must contain a list of transactions")

            return data

    except FileNotFoundError:
        print("File not found")
        return [{}]
    except json.decoder.JSONDecodeError:
        print("Invalid json file")
        return [{}]
    except ValueError as e:
        print(e)
        return [{}]
