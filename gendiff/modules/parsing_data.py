import json
import yaml


formats = {
    'json': json.load,
    'yaml': yaml.safe_load,
    'yml': yaml.safe_load
}


def parse_data(file_path):
    """
    Open files of json, yaml, yml formats
    """
    _, extension = file_path.split('.')
    if extension not in formats:
        raise ValueError(
            'Unsupported format. Next formats are supported: {}'.format(
                ', '.join(formats)))

    return formats[extension](open(file_path))
