class Solution(object):
    def maxArea(self, height):
        MaxArea = 0
        i = 0
        j = len(height) - 1

        while i < j:
            a = height[i]
            b = height[j]

            if a <= b:
                area = (j-i) * a
                i = i+1
            else:
                area = (j-i) * b
                j = j-1
            
            if MaxArea < area:
                MaxArea = area
        return MaxArea


height =[1,8,6,2,5,4,8,3,7]
obj = Solution()
print(obj.maxArea(height))




# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
# Example 2:

# Input: height = [1,1]
# Output: 1
 