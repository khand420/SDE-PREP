class Solution:
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