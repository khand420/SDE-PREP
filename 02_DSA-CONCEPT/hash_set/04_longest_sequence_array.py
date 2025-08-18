# Find the longest consecutive sequence in an array

def longestConsecutive(nums):
    num_set = set(nums)
    length = 0
    for start in nums:
        if start - 1 not in num_set:
            end = start + 1
            while end in num_set:
                end += 1
            length = max(length, end - start)
    return length



nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
# Example 2:

# nums = [0,3,7,2,5,8,4,6,0,1]
# Output: 9

print(longestConsecutive(nums))