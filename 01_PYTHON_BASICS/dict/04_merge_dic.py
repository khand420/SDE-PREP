dict1 = {"a": 1}
dict2 = {"b": 2}
dict3 = {"c": 3}
dict4 = {"b": 3}

merged_dict = {**dict1, **dict2, **dict3, **dict4}  # Merging

print(merged_dict)



d1 = {'k1': 2, 'k2': 3, 'k3': 3, 'k4': 4, 'k5': 5}
d2 = {'k1': 4, 'k6': 3, 'k3': 10, 'k7': 4, 'k8': 5}

# Create a new dictionary to hold the merged results
merged_dict = {}

# Add values from the first dictionary
for key, value in d1.items():
    merged_dict[key] = value

# Add values from the second dictionary
for key, value in d2.items():
    if key in merged_dict:
        merged_dict[key] += value  # Sum the values if the key exists
    else:
        merged_dict[key] = value  # Add the key-value pair if it doesn't exist

print(merged_dict)
