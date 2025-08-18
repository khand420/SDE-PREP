# def findPath(mat, r, c, path, ans):
#     n = len(mat)

#     # Base Conditions
#     if r < 0 or c < 0 or r >= n or c >= n or mat[r][c] != 1:
#         return

#     # Destination reached
#     if r == n - 1 and c == n - 1:
#         ans.append(path)
#         return

#     mat[r][c] = -1  # Mark as visited

#     # Explore all directions
#     findPath(mat, r + 1, c, path + "D", ans)  # Down
#     findPath(mat, r - 1, c, path + "U", ans)  # Up
#     findPath(mat, r, c + 1, path + "R", ans)  # Right
#     findPath(mat, r, c - 1, path + "L", ans)  # Left

#     mat[r][c] = 1  # Unmark (Backtrack)


# # Driver Code
# mat = [[1, 0, 0, 0],
#        [1, 1, 0, 1],
#        [1, 1, 0, 0],
#        [0, 1, 1, 1]]
# ans = []
# findPath(mat, 0, 0, "", ans)
# ans.sort()
# print(ans)




# Input: mat[][] = [[1, 0, 0, 0], [1, 1, 0, 1], [1, 1, 0, 0], [0, 1, 1, 1]]
# Output: ["DDRDRR", "DRDDRR"]
# Explanation: The rat can reach the destination at (3, 3) from (0, 0) by two paths - DRDDRR and DDRDRR, when printed in sorted order we get DDRDRR DRDDRR.





import time

# Get the current Unix timestamp
current_timestamp = int(time.time())
print(current_timestamp)