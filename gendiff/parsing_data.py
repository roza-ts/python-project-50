import json
import yaml


formats = {
    'json': json.load,
    'yaml': yaml.safe_load,
    'yml': yaml.safe_load
    }


def parsing_data(path):
    """
    Сonverts files of different formats into a Python dictionary
    """
    _, extension = path.split('.')
    if extension not in formats:
        raise ValueError(f'Unsupported format. Next formats are supported:
        {', '.join(formats)}')
    return formats[extension](open(path))
