from math import ceil


class Solution:
    def minEatingSpeed(self, piles, h):
        def hours_needed(speed):
            return sum((pile + speed - 1) // speed for pile in piles)

        left, right = 1, max(piles)

        while left < right:
            mid = (left + right) // 2
            if hours_needed(mid) <= h:
                right = mid
            else:
                left = mid + 1

        return left

piles = [3,6,7,11]
h = 8
piles = [30,11,23,4,20]
h = 5
koko = Solution()


print(koko.minEatingSpeed(piles, h))

# class Solution:
#     def minEatingSpeed(self, piles, h):
#         left = 1
#         right = max(piles)
#         result = right
        
#         while left <= right:
#             mid = left + (right - left) // 2
#             total = sum([ceil(pile / mid) for pile in piles])
            
#             if total <= h:
#                 result = mid
#                 right = mid -1
#             else:
#                 left = mid + 1
#         return result




# Example 1:

# Input: piles = [3,6,7,11], h = 8
# Output: 4
# Example 2:

# Input: piles = [30,11,23,4,20], h = 5
# Output: 30
# Example 3:

# Input: piles = [30,11,23,4,20], h = 6
# Output: 23
 