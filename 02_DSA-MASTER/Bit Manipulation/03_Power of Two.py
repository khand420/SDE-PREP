class Solution(object):
    def isPowerOfTwo(self, n):
        while(n%2==0 and n!=0):
            n=n/2
        return n==1
    

obj = Solution()
print(obj.isPowerOfTwo(17))