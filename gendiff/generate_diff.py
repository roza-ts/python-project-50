import json


def generate_diff(path1, path2):
    file1 = json.load(open(path1))
    file2 = json.load(open(path2))
    dct = {}

    for key, value in file1.items():
        if key in file2:
            if value == file2[key]:
                dct[key] = value
            else:
                dct[f'{key} minus'] = value
                dct[f'{key} plus'] = file2[key]
        else:
            dct[f'{key} minus'] = value

    for key, value in file2.items():
        if key not in dct and f'{key} plus' not in dct:
            dct[f'{key} plus'] = file2[key]
    keys = sorted(list(dct.keys()))
    dct = {key: dct[key] for key in keys}

    return stringify_dict(dct)


def stringify_dict(dct):
    res = ['{']
    for key, value in dct.items():
        if value is True or value is False:
            value = ('false', 'true')[value is True]
        if 'minus' in key:
            elem = f' - {key[:-6]}: {value}'
        elif 'plus' in key:
            elem = f' + {key[:-5]}: {value}'
        else:
            elem = f'   {key}: {value}'
        res.append(elem)
    res.append('}')
    return '\n'.join(res)
