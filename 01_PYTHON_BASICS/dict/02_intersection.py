dict1 = {"a": 1, "b": 2}
dict2 = {"x": 2, "y": 3}
intersection = set(dict1.values()) & set(dict2.values())
# intersection = dict1 & dict2


merged_dict = dict1 | dict2  

print(intersection)
print(merged_dict)
