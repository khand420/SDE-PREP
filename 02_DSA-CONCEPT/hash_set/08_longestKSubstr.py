# Python program to find the longest substring
# with k unique characters in a given string

# Function to calculate length of
# longest substring with k characters
def longestKSubstr(s, k):
	n = len(s)
	answer = -1
	for i in range(n):
		for j in range(i+1, n+1):
			distinct = set(s[i:j])
			if len(distinct) == k:
				answer = max(answer, j - i)
	print(answer)

s = "aabacbebebe"
k = 3

# Function Call
longestKSubstr(s, k)







# def longestKDistinctSubstr(s, k):
#     n = len(s)
#     left = 0
#     char_count = {}
#     max_length = 0

#     for right in range(n):
#         char_count[s[right]] = char_count.get(s[right], 0) + 1

#         while len(char_count) > k:
#             char_count[s[left]] -= 1
#             if char_count[s[left]] == 0:
#                 del char_count[s[left]]
#             left += 1

#         max_length = max(max_length, right - left + 1)

#     return max_length

# s = "aabacbebebe"
# k = 3

# # Function Call
# result = longestKDistinctSubstr(s, k)
# print(result)
