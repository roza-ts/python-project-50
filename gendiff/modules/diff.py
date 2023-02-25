def get_diff(dict1, dict2):
    diff_dict = {}
    for key, value in dict1.items():
        if key in dict2:
            value2 = dict2[key]
            if isinstance(value, dict) and isinstance(value2, dict):
                diff_dict[key] = get_diff(value, value2)
            else:
                if value == value2:
                    diff_dict[f'{key}'] = value
                else:
                    diff_dict[f'{key} minus_upd'] = value
                    diff_dict[f'{key} plus_upd'] = value2
        else:
            diff_dict[f'{key} minus'] = value
    add_dict(dict1, dict2, diff_dict)
    keys = sorted(diff_dict.keys())
    diff_dict = {key: diff_dict[key] for key in keys}
    return diff_dict


def add_dict(dict1, dict2, diff_dict):
    for key, value in dict2.items():
        if key not in dict1:
            diff_dict[f'{key} plus'] = value
