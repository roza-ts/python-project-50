from gendiff.modules.stylish import normalize_value


def plain(dct, begin=''):
    res = []
    old_value = None
    for key, value in dct.items():
        if 'minus' in key or 'plus' in key:
            key, addition = key.split()
            value = get_value(value)
            descriptions = {
                'plus_upd': f"Property '{begin}{key}' was updated. From {old_value} to {value}",  # noqa
                'minus': f"Property '{begin}{key}' was removed",
                'plus': f"Property '{begin}{key}' was added with value: {value}"
            }
            if addition == 'minus_upd':
                old_value = value
            else:
                res.append(descriptions[addition])
        else:
            if isinstance(value, dict):
                begin += f'{key}.'
                res.append(plain(value, begin))
                begin = begin.replace(f'{key}.', '')
    return '\n'.join(sorted(res))


def get_value(value):
    value = normalize_value(value)
    if isinstance(value, (dict, list, set, tuple)):
        return '[complex value]'
    if isinstance(value, (int, float)) or value in ('true', 'false', 'null'):
        return value
    return f"'{value}'"
