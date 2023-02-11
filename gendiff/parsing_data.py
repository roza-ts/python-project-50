import json
import yaml


formats = {
          'json': json.load,
          'yaml': yaml.safe_load,
          'yml': yaml.safe_load
          }


def parsing_data(path):
    _, form = path.split('.')

    if form not in formats:
        print()
    return formats[form](open(path))
