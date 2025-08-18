# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
# print("Try programiz.pro")
# You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string. 
# Return the merged string. 

# Example 1: 
# Input: word1 = "abc", word2 = "pqr"Output:
# "apbqcr"Explanation: The merged string will be merged as so: 
# word1:  a   b   c 
# word2:    p   q   r 
# merged: a p b q c r


def merge_strings(word1, word2):
    merged = []
    length = max(len(word1), len(word2))
    
    for i in range(length):
        if i < len(word1):
            merged.append(word1[i])
        if i < len(word2):
            merged.append(word2[i])
    
    return ''.join(merged)

# Example usage
word1 = "abc"
word2 = "pqr"
result = merge_strings(word1, word2)
print(result)  # Output: "apbqcr"


# word1 = "abc"
# word2 = "pqr"
# # Output:"apbqcr"
# print(merge_string(word1, word2))


# The words in s will be separated by at least one space. 
# Return a string of the words in reverse order concatenated by a single space. 
# Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces. 
#   
# Example 1: 
# Input: s = "the sky is blue"
# Output: "blue is sky the"


def rev(s):
    lst = [x for x in s.split(" ") ] #" "
    # s.split(" ")[::-1]
  
    # print("-------- ",lst[::-1])
    lst.reverse()
    return lst
    # s = reversed(s)
    # # print(s)
    # arr=  []
    # for i in s.split()[::-1]:
    #     arr.append(i)
    #     # print((i))
    # return reversed(arr)
    # return "".join(s)

    # print(arr)    





s = "the sky is blue"
print(rev(s))