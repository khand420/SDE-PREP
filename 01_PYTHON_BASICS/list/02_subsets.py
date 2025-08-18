# ### 4. `combinations(iterable, r)`
# - **Definition**: Returns all possible combinations of `r` elements from the iterable, without replacement.
# - **Use Case**: Useful in scenarios such as selecting teams or creating unique sets of items.
# - **Example**:
#   ```python
#   from itertools import combinations

#   items = ['A', 'B', 'C', 'D']
#   print(list(combinations(items, 2)))  
#   # Outputs



def subsetsWithDup(nums):
    nums.sort()  # Sort the input to handle duplicates
    result =[] #set()  # Use a set to avoid duplicates
    for i in range(len(nums)):
        # for j in range(i+1, len(nums)+1):
        for j in range(0, len(nums)+1):
            # result.add(nums[i]+nums[j]) 
            # result.append(nums[i:j]) 
            if not nums[i:j] in result:
                result.append(nums[i:j]) 

    return result
# Example usage
nums = [1, 2, 2]
print(subsetsWithDup(nums))


from itertools import combinations

def subsetsWithDup(nums):
    nums.sort()  # Sort the input to handle duplicates
    result = set()  # Use a set to avoid duplicates
    
    # Generate combinations of all lengths
    for i in range(len(nums) + 1):
        for combo in combinations(nums, i):
            result.add(combo)  # Add the combination to the set

    print(list(result))          
    # Convert the set back to a list of lists
    return [list(subset) for subset in result]

# Example usage
nums = [1, 2, 2]
print(subsetsWithDup(nums))







# def subsetsWithDup(nums):
#     # Sort the list to handle duplicates
#     nums.sort()
#     # Initialize with the empty subset
#     result = [[]]
    
#     # Start from the first index
#     start = 0
    
#     for i in range(len(nums)):
#         # If we're at the start or the current number is not a duplicate of the previous number
#         if i == 0 or nums[i] != nums[i - 1]:
#             start = 0  
#         # Capture the number of subsets to extend
#         size = len(result)
#         # For each subset currently in result, add the current number to it
#         for j in range(start, size):
#             result.append(result[j] + [nums[i]])
#         # Update start to the index where the current number starts to avoid duplicates
#         start = size
    
#     return result

# # Example usage
# nums = [1, 2, 2]
# print(subsetsWithDup(nums))







# def subsetsWithDup(nums):
#     def backtrack(start, path):
#         # Add a copy of the current subset to the result
#         res.append(path[:])
#         # Iterate through the list starting from the index `start`
#         for i in range(start, len(nums)):
#             # Skip duplicates: only include `nums[i]` if it's not the same as the previous element
#             if i > start and nums[i] == nums[i - 1]:
#                 continue
#             # Include the current number in the subset
#             path.append(nums[i])
#             # Recurse to generate subsets that include the current number
#             backtrack(i + 1, path)
#             # Remove the last added number (backtrack) to explore other subsets
#             path.pop()

#     # Sort the numbers to handle duplicates
#     nums.sort()
#     res = []
#     backtrack(0, [])  # Start with an empty subset
#     return res

# # Example usage
# nums = [1, 2, 2]
# print(subsetsWithDup(nums))







