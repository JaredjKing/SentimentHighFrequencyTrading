import json

def load_api_keys(filepath="config/api_keys.json"):
    with open(filepath, "r") as f:
        return json.load(f)
