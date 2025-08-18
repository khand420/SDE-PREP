# def longest_common_prefix(s):
#     # Check if the list is empty
#     if not s:
#         return ""

#     # Use the first string as a reference
#     for i in range(len(s[0])):
#         current_char = s[0][i]
        
#         # Compare with each string
#         for string in s[1:]:
#             # If index exceeds the length of the string or characters do not match
#             if i >= len(string) or string[i] != current_char:
#                 return s[0][:i]  # Return the common prefix found so far

#     return s[0]  # All characters matched, return the whole first string

# # Example usage
# s = ["flower", "flow", "flight"]
# result = longest_common_prefix(s)
# print(result)  # Output: "fl"





# def longest_common_prefix(s):
#     # Check if the list is empty
#     if not s:
#         return ""

#     # Find the length of the shortest string
#     min_length = min(len(string) for string in s)

#     # Binary search for the longest common prefix length
#     low, high = 0, min_length

#     while low <= high:
#         mid = (low + high) // 2
#         prefix = s[0][:mid]

#         # Check if all strings have the same prefix of length mid
#         if all(string.startswith(prefix) for string in s):
#             low = mid + 1  # Move to the right half
#         else:
#             high = mid - 1  # Move to the left half

#     return s[0][: (low + high) // 2]  # Return the longest common prefix

# # Example usage
# s = ["flower", "flow", "flight"]
# result = longest_common_prefix(s)
# print(result)  # Output: "fl"





# def longest_common_prefix(strs):
#     if not strs:
#         return ""
#     prefix = strs[0]
#     for i in strs[1:]:
#         while not i.startswith(prefix):
#             prefix = prefix[:-1]
#     return prefix


# strs = ["flower", "flow", "flight"]
# print(longest_common_prefix(strs))



