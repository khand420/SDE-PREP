def longest_substring_without_duplicates(s):
    char_set = set()
    left = max_length = 0

    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        char_set.add(s[right])
        max_length = max(max_length, right - left + 1)

    return max_length

s = "zxyzxyz"
print(longest_substring_without_duplicates(s))  # Output: 3




# def longest_substring_without_duplicates(s):
#     char_set = set()
#     left = 0
#     max_length = 0
#     start_index = 0  # To track the starting index of the longest substring

#     for right in range(len(s)):
#         # If the character is already in the set, move the left pointer
#         while s[right] in char_set:
#             char_set.remove(s[left])
#             left += 1
#         # Add the current character to the set
#         char_set.add(s[right])
        
#         # Update the maximum length found and the starting index
#         if right - left + 1 > max_length:
#             max_length = right - left + 1
#             start_index = left

#     # Extract the longest substring
#     longest_substring = s[start_index:start_index + max_length]

#     return max_length, longest_substring

# s = "zxyzxyz"
# length, substring = longest_substring_without_duplicates(s)
# print(f"Length: {length}, Substring: '{substring}'")  # Output: Length: 3, Substring: 'xyz'



# Summary of Easy Solutions:
# Longest Consecutive Sequence: Use a set to quickly check for the existence of numbers and count sequences.
# Longest Substring Without Duplicates: Use a sliding window approach with a set to track characters and maintain the current substring.
# These easy solutions are efficient and 