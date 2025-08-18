class Solution:
    def isSafe(self, board, row, col, n):
        # H
        for j in range(n):
            if board[row][j] == 'Q':
                return False
        # V
        for j in range(n):
            if board[j][col] == 'Q':
                return False
        # left Side Diagonal
        i, j = row, col
        while i >= 0 and j >= 0:
            if board[i][j] == 'Q':
                return False
            i -= 1
            j -= 1
        # right side diagonal
        i, j = row, col
        while i >= 0 and j < n:
            if board[i][j] == 'Q':
                return False
            i -= 1
            j += 1
        return True

    def nQueen(self, board, row, n, ans):
        if row == n:
            ans.append(board[:])
            return

        for j in range(n):
            if self.isSafe(board, row, j, n):
                board[row] = board[row][:j] + 'Q' + board[row][j+1:]
                self.nQueen(board, row + 1, n, ans)
                board[row] = board[row][:j] + '.' + board[row][j+1:]

    def solveNQueens(self, n):
        board = ["." * n for i in range(n)]
        ans = []
        self.nQueen(board, 0, n, ans)
        return ans


obj = Solution()

print(obj.solveNQueens(4))



# Input: n = 4
# Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
# Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above
# Example 2:

# Input: n = 1
# Output: [["Q"]]
