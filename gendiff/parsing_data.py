import json
import yaml


def parsing_data(path):
    if path.endswith('.json'):
        return json.load(open(path))

    elif path.endswith('.yaml') or path.endswith('yml'):
        return yaml.safe_load(open(path))
