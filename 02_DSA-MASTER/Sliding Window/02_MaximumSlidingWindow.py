
def maxSlidingWindow( nums, k):
    from collections import deque
    q = deque() # stores *indices*
    res = []
    for i, cur in enumerate(nums):
        while q and nums[q[-1]] <= cur:
            q.pop()
        q.append(i)
        # remove first element if it's outside the window
        if q[0] == i - k:
            q.popleft()
        # if window has k elements add to results (first k-1 windows have < k elements because we start from empty window and add 1 element each iteration)
        if i >= k - 1:
            res.append(nums[q[0]])
    return res




from collections import deque
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()
        ans = []
        i, j = 0, 0

        # Fill the first window
        while i - j != k:
            while dq and nums[dq[0]] < nums[i]:
                dq.popleft()
            dq.appendleft(i)
            i += 1
        ans.append(nums[dq[-1]])

        # Slide the window
        while i < len(nums):
            if dq[-1] == j:
                dq.pop()
            j += 1
            while dq and nums[dq[0]] < nums[i]:
                dq.popleft()
            dq.appendleft(i)
            i += 1
            ans.append(nums[dq[-1]])

        return ans
# Example 1:

# Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
# Output: [3,3,5,5,6,7]
# Explanation: 
# Window position                Max
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
#  1 [3  -1  -3] 5  3  6  7       3
#  1  3 [-1  -3  5] 3  6  7       5
#  1  3  -1 [-3  5  3] 6  7       5
#  1  3  -1  -3 [5  3  6] 7       6
#  1  3  -1  -3  5 [3  6  7]      7
# Example 2:

# Input: nums = [1], k = 1
# Output: [1]