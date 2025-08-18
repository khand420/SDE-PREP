def flatten_list(nested_list):
    strs = ''.join(str(nested_list))
    flat_list = []
    for i in strs:
        if i.isnumeric():
            flat_list.append(int(i))

    # flat_list = []
    # for item in nested_list:
    #     if isinstance(item, list):
    #         flat_list.extend(flatten_list(item))
    #     else:
    #         flat_list.append(item)
    return flat_list

print(flatten_list([1, 2, [3, 4, [5, 6]]]))