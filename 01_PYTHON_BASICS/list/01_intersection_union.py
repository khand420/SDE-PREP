def intersection(list1, list2):

    return list(set(list1) & set(list2)) #intersection [3, 4]
    # return list(set(list1) | set(list2)) #union [1, 2, 3, 4, 5, 6]





list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
print(intersection(list1, list2))