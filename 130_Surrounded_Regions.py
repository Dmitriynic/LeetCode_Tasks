#130 Surrounded Regions

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        def func_(i, j):
            board[i][j] = 'OO'
            if i < len(board) - 1 and board[i+1][j] == 'O':
                func_(i + 1, j)
            if i > 0 and board[i - 1][j] == 'O':
                func_(i - 1, j)
            if j > 0 and board[i][j - 1] == 'O':
                func_(i, j - 1)
            if j < len(board[0]) - 1 and board[i][j + 1] == 'O':
                func_(i, j + 1)
                
        for i in range(len(board)):
            if board[i][0] == 'O':
                func_(i, 0)
            if board[i][len(board[0]) - 1] == 'O':
                func_(i, len(board[0]) - 1)
        for j in range(len(board[0])):
            if board[0][j] == 'O':
                func_(0, j)
            if board[len(board) - 1][j] == 'O':
                func_(len(board) - 1, j)
                
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'OO':
                    board[i][j] = 'O'
                else:
                    board[i][j] = 'X'

#122ms, faster than 49.92%, memory 17.9MB less than 84.66%
