from collections import defaultdict
def groupAnagrams(strs):
    # anagram_map = defaultdict(list)
    
    # for word in strs:
    #     sorted_word = ''.join(sorted(word))
    #     anagram_map[sorted_word].append(word)
    
    # return list(anagram_map.values())


    anagram_dict = {}
    
    for word in strs:
        sorted_word = ''.join(sorted(word))
        if sorted_word not in anagram_dict:
            anagram_dict[sorted_word] = []
        anagram_dict[sorted_word].append(word)
        
    return list(anagram_dict.values())

strs = ["eat","tea","tan","ate","nat","bat"]

print(groupAnagrams(strs))






# Example 1:

# Input: strs = ["eat","tea","tan","ate","nat","bat"]

# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

# Explanation:

# There is no string in strs that can be rearranged to form "bat".
# The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
# The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.
# Example 2:

# Input: strs = [""]

# Output: [[""]]

# Example 3:

# Input: strs = ["a"]

# Output: [["a"]]

 