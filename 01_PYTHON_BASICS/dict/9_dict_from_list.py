data = [("a", 1), ("b", 2), ("c", 3)]

nested_dict = {}
# for key, value in data:
#     nested_dict.setdefault(key, {}).update({"value": value})
print(nested_dict)  

# -------------------------------------------------

list_of_tuples = [('a', 1), ('b', 2), ('c', 3)]

dictionary = {key: value for key, value in list_of_tuples}
print(dictionary)

# ----------------------------------------

lst = ['a', 1, 'b', 2, 'c', 3]
d =  {}
for i in range(0, len(lst), 2):
    d[lst[i]] = lst[i+1]

print(d)  

# -----------------------------------------------

keys = ['a', 'b', 'a', 'c']
values = [1, 2, 3, 4]

dictionary = dict(zip(keys, values))
# new_dict = {stocks: prices for stocks,
#             prices in zip(keys, values)}
# print(new_dict)
print(dictionary)