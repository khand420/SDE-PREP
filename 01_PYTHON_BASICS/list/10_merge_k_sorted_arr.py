def flatten(lst):
    flat_list = []
    for item in lst:
        if isinstance(item, list):
            flat_list.extend(flatten(item))
        else:
            flat_list.append(item)
    return sorted(flat_list)

lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
print(flatten(lists))  # Output: [1, 1, 2, 3, 4, 4, 5, 6]