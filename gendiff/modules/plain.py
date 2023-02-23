def plain(dct, begin=''):
    res = []
    for key, value in dct.items():
        if 'minus' in key or 'plus' in key:
            value = get_value(value)
            key, inf = key.split()
            if inf == 'minus_upd':
                old_value = value
            elif inf == 'plus_upd':
                res.append(f"Property '{begin}{key}' was updated. From {old_value} to {value}")
            elif inf == 'minus':
                res.append(f"Property '{begin}{key}' was removed")
            elif inf == 'plus':
                res.append(f"Property '{begin}{key}' was added with value: {value}")
        else:
            if isinstance(value, dict):
               begin += f'{key}.'
               res.append(plain(value, begin))
               begin = begin.replace(f'{key}.', '')

    return '\n'.join(sorted(res))


def get_value(value):
    if isinstance(value, dict):
        return '[complex value]'
    if value in (True, False, None):
        return {True: 'true', False: 'false', None: 'null'}[value]
    return f"'{value}'"
