from collections import deque
class Solution(object):
    def firstUniqChar(self, s):
        queue = deque()
        dic = {}

        # Step 1: Count frequencies and maintain queue
        for i, ch in enumerate(s):
            dic[ch] = dic.get(ch, 0) + 1
            queue.append((ch, i))  # Store character and its index

            # Remove characters from front of queue until it's unique
            while queue and dic[queue[0][0]] > 1:
                queue.popleft()

        # Step 2: Check result
        if queue:
            return queue[0][1]  # Return index of first unique character
        return -1


sol = Solution()
print(sol.firstUniqChar("leetcode"))      # Output: 0 (l)
print(sol.firstUniqChar("loveleetcode"))  # Output: 2 (v)
print(sol.firstUniqChar("aabb"))          # Output: -1 (none)
