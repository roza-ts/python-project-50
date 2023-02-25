def stylish(dct, depth=1):
    indent = '    '
    res = ['{']
    for key, value in dct.items():
        if isinstance(value, dict):
            depth += 1
            value = stylish(value, depth)
            depth -= 1
        value = normalize_value(value)
        filling = indent * depth
        if 'minus' in key or 'plus' in key:
            key, addition = key.split()
            if 'minus' in addition:
                extention = ' - '
            elif 'plus' in addition:
                extention = ' + '
        else:
            extention = '   '
        filling = filling[:-3] + extention
        res.append(filling + f'{key}: {value}')
    last_string = indent * (depth - 1) + '}'
    res.append(last_string)
    return '\n'.join(res)


def normalize_value(value):
    if isinstance(value, (bool, type(None))):
        value = {True: 'true', False: 'false', None: 'null'}[value]
    return value
