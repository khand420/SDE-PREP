sorted_dict = dict(sorted({"a": 3, "b": 1, "c": 2}.items(), key=lambda item: item[1]))  # {'b': 1, 'c': 2, 'a': 3}
print(sorted_dict)