from gendiff.modules.diff import get_diff
from gendiff.modules.stylish import stylish
from gendiff.modules.plain import plain
from gendiff.modules.json import get_json
from gendiff import parse_data


def generate_diff(file_path1, file_path2, formatter=stylish):
    dict1, dict2 = parse_data(file_path1), parse_data(file_path2)
    diff_dict = get_diff(dict1, dict2)
    if formatter == 'plain':
        return plain(diff_dict)
    if formatter == 'json':
        return get_json(diff_dict)
    return stylish(diff_dict)
