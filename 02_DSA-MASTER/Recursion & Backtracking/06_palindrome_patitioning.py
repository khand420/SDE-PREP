def isPal(s):
    return s == s[::-1]

def getAllPalindrome(s, partition, ans):
    # Base case: if the string is empty, add the current partition to the answer
    if len(s) == 0:
        ans.append(partition[:])  # Use append to add a copy of the partition
        return
    
    # Iterate through the string to find all palindromic partitions
    for i in range(len(s)):
        part = s[:i + 1]  # Use slicing to get the substring
        if isPal(part):
            partition.append(part)  # Use append to add the palindromic part

            # Recur for the remaining substring
            getAllPalindrome(s[i + 1:], partition, ans)
            partition.pop()  # Backtrack

# Example usage
s = "aab"
partition = [] 
ans = []

getAllPalindrome(s, partition, ans)

print(ans)  # Output: [['a', 'a', 'b'], ['aa', 'b']]






# Example 1:

# Input: s = "aab"
# Output: [["a","a","b"],["aa","b"]]
# Example 2:

# Input: s = "a"
# Output: [["a"]]
