def flatten_dict(d, parent_key='', sep='_'):
    items = {}
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.update(flatten_dict(v, new_key, sep=sep))
        else:
            items[new_key] = v
    return items

# Example
nested_dict = {"a": 1, "b": {"c": 2, "d": 3}}
print(flatten_dict(nested_dict))  # {'a': 1, 'b_c': 2, 'b_d': 3}