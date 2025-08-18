# Example 1:

# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.
# Example 2:

# Input: s = "cbbd"
# Output: "bb"

class Solution:
    def longestPalindrome(self, s: str) -> str:
        n=len(s)
        def expand_pallindrome(i,j):            
            while 0<=i<=j<n and s[i]==s[j]:
                i-=1
                j+=1                            
            return (i+1, j)
        
        res=(0,0)
        for i in range(n):
            b1 = expand_pallindrome(i,i)
            b2 = expand_pallindrome(i,i+1)            
            res=max(res, b1, b2,key=lambda x: x[1]-x[0]+1) # find max based on the length of the pallindrome strings.
                    
        return s[res[0]:res[1]]    
    


class Solution:
    def longestPalindrome(self, s: str) -> str:
        n=len(s)
        def expand_center(i,j):            
            while 0<=i<=j<n and s[i]==s[j]:
                i-=1
                j+=1                
            
            return (i+1, j)                
        
        res=max([expand_center(i,i+offset) for i in range(n) for offset in range(2)], key=lambda x: x[1]-x[0]+1)
        
        return s[res[0]:res[1]]