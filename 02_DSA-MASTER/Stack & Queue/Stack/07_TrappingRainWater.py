class Solution(object):
    def trap(self, height):

        if not height:
            return 0

        n = len(height)
        left_max = [0] * n
        right_max = [0] * n

        # Fill left_max
        left_max[0] = height[0]
        for i in range(1, n):
            left_max[i] = max(height[i], left_max[i - 1])

        # Fill right_max
        right_max[n - 1] = height[n - 1]
        for i in range(n - 2, -1, -1):
            right_max[i] = max(height[i], right_max[i + 1])

        # Calculate trapped water
        water = 0
        for i in range(n):
            water += min(left_max[i], right_max[i]) - height[i]
        
        print("Left Max:", left_max)
        print("Right Max:", right_max)
        print("Water Trapped:", water)
        return water


        # n = len(height) - 1
        # l, r = 0, n
        # lmax, rmax = 0, 0
        # w = 0
        
        # while l < r:
        #     lmax = max(lmax, height[l])
        #     rmax = max(rmax, height[r])

        #     if lmax < rmax:
        #         w += lmax - height[l]            
        #         l += 1
        #     else:
        #         w += rmax - height[r]
        #         r -= 1
                
        # return w

# Example usage
# height = [0,1,0,2,1,0,1,3,2,1,2,1]
height = [4,2,0,3,2,5]
solution = Solution()
print(solution.trap(height))  # Output: 6
# Explanation: The water trapped between the bars is 6 units.
# The bars are represented by the height array, and the water is trapped in the valleys formed
# between the bars.
# In this case, the water is trapped at indices 2, 3, 4     # and 6, resulting in a total of 6 units of water.
# The left pointer moves to the right, and the right pointer moves to the left, calculating
# the trapped water at each step based on the maximum heights encountered so far.
# The algorithm efficiently calculates the trapped water in O(n) time complexity and O(1)
# space complexity, making it suitable for large input sizes.       