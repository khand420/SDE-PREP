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


# from itertools import combinations

# def subsetsWithDup(nums):
#     nums.sort()  # Sort the input to handle duplicates
#     result = set()  # Use a set to avoid duplicates
    
#     # Generate combinations of all lengths
#     for i in range(len(nums) + 1):
#         for combo in combinations(nums, i):
#             result.add(combo)  # Add the combination to the set

#     print(list(result))          
#     # Convert the set back to a list of lists
#     return [list(subset) for subset in result]

# # Example usage
# nums = [1, 2, 2]
# print(subsetsWithDup(nums))
# # Output: 1

# from itertools import permutations

# items = ['A', 'B', 'C']
# print(list(permutations(items, 2)))  
# # Outputs: [('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'C'), ('C', 'A'), ('C', 'B')]



# def subsetsWithDup(nums):
#     result = []
#     nums.sort()  # Sort to handle duplicates
#     def backtrack(start, path):
#         result.append(path)  # Add the current subset
#         for i in range(start, len(nums)):
#             if i > start and nums[i] == nums[i - 1]:  # Skip duplicates
#                 continue
#             backtrack(i + 1, path + [nums[i]])  # Include nums[i] in the subset

#     backtrack(0, [])
#     return result

# # Example usage
# nums = [1, 2, 2]
# output = subsetsWithDup(nums)
# print(output)
