from gendiff.modules.diff import get_diff_dict
from gendiff.modules.stylish import stylish
from gendiff.modules.plain import plain
from gendiff.modules.parsing_data import parse_data


def generate_diff(file_path1, file_path2, formater=stylish):
    dict1, dict2 = parse_data(file_path1), parse_data(file_path2)
    diff_dict = get_diff_dict(dict1, dict2)
    if formater == 'plain':
        return plain(diff_dict)
    return stylish(diff_dict)
    #return diff_dict
