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
