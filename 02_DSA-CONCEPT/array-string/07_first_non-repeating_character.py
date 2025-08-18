# Example 1:

# Input: s = "leetcode"
# Output: 0
# Example 2:

# Input: s = "loveleetcode"
# Output: 2
# Example 3:

# Input: s = "aabb"
# Output: -1


def firstUniqChar(s):

    char_count = {}
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    # Step 2: Find the first character with a count of 1
    for index, char in enumerate(s):
        if char_count[char] == 1:
            return index
    
    # If no non-repeating character is found, return -1
    return -1   


s = "loveleetcode"

print(firstUniqChar(s))