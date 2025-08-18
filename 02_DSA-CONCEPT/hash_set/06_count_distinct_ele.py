# # Count distinct elements in every window of size k.


# from collections import defaultdict

# def count_distinct_in_windows(arr, k):
#     if k > len(arr):
#         return []

#     count_map = defaultdict(int)
#     distinct_counts = []
    
#     # Initialize the first window
#     for i in range(k):
#         count_map[arr[i]] += 1
    
#     # Count distinct elements in the first window
#     distinct_counts.append(len(count_map))

#     # Slide the window
#     for i in range(k, len(arr)):
#         # Add new element to the window
#         count_map[arr[i]] += 1
        
#         # Remove the element that is sliding out of the window
#         count_map[arr[i - k]] -= 1
        
#         # If the count becomes zero, remove it from the map
#         if count_map[arr[i - k]] == 0:
#             del count_map[arr[i - k]]
        
#         # Count distinct elements in the current window
#         distinct_counts.append(len(count_map))
    
#     return distinct_counts

# # Example usage:
# arr = [1, 2, 1, 3, 4, 2, 3]
# k = 3
# result = count_distinct_in_windows(arr, k)
# print(result)  # Output: [2, 3, 3, 2]




from collections import Counter

def count_distinct_in_windows(arr, k):
    if k > len(arr):
        return []

    # Initialize the counter with the first window
    count_map = Counter(arr[:k])
    distinct_counts = [len(count_map)]

    # Slide the window
    for i in range(k, len(arr)):
        # Add the new element
        count_map[arr[i]] += 1
        
        # Remove the element that is sliding out of the window
        count_map[arr[i - k]] -= 1
        
        # If the count becomes zero, remove it from the counter
        if count_map[arr[i - k]] == 0:
            del count_map[arr[i - k]]
        
        # Count distinct elements in the current window
        distinct_counts.append(len(count_map))
    
    return distinct_counts

# Example usage:
arr = [1, 2, 1, 3, 4, 2, 3]
k = 3
result = count_distinct_in_windows(arr, k)
print(result)  # Output: [2, 3, 3, 2]
