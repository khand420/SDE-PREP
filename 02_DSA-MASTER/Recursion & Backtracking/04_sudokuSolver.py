# class Solution:
#     def solveSudoku(self, board):
#         def solve():
#             for row in range(9):
#                 for col in range(9):
#                     if board[row][col] == '.':
#                         for num in '123456789':
#                             if is_valid(row, col, num):
#                                 board[row][col] = num
#                                 if solve():
#                                     return True
#                                 board[row][col] = '.'
#                         return False
#             return True

#         def is_valid(row, col, num):
#             for i in range(9):
#                 if board[row][i] == num or board[i][col] == num:
#                     return False
#             start_row, start_col = 3 * (row // 3), 3 * (col // 3)
#             for i in range(start_row, start_row + 3):
#                 for j in range(start_col, start_col + 3):
#                     if board[i][j] == num:
#                         return False
#             return True

#         solve()


# obj = Solution()
# board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
# # print(obj.solveSudoku(board))
# # obj.solveSudoku(board)

# solved_board = obj.solveSudoku(board)
# for row in solved_board:
#     print(row)




# Input: board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
# Output: [["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1","7","9"]]
# Explanation: The input board is shown above and the only valid solution is shown below:



class Solution:
    def solveSudoku(self, board):
        def solve():
            for row in range(9):
                for col in range(9):
                    if board[row][col] == '.':
                        for num in '123456789':
                            if is_valid(row, col, num):
                                board[row][col] = num
                                if solve():
                                    return True
                                board[row][col] = '.'
                        return False
            return True

        def is_valid(row, col, num):
            for i in range(9):
                if board[row][i] == num or board[i][col] == num:
                    return False
            start_row, start_col = 3 * (row // 3), 3 * (col // 3)
            for i in range(start_row, start_row + 3):
                for j in range(start_col, start_col + 3):
                    if board[i][j] == num:
                        return False
            return True

        solve()
        return board  # Return the solved board

# Example usage
obj = Solution()
board = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]

solved_board = obj.solveSudoku(board)
for row in solved_board:
    print(row)
