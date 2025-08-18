def first_repeating_element(arr):
    seen = set()
    for i in arr:
        if i in seen:
            return i
        else:
            seen.add(i)
    return None        


# Example usage:
arr = [1, 2, 3, 4, 2, 5]
result = first_repeating_element(arr)
print(result)  # Output: 2