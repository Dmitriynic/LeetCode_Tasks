#36 Valid Sudoku

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            dict_row = defaultdict(int)
            for j in range(9):
                if board[i][j] != '.':
                    dict_row[board[i][j]] += 1
                    if dict_row[board[i][j]] > 1:
                        return False
        for j in range(9):
            dict_col = defaultdict(int)
            for i in range(9):
                if board[i][j] != '.':
                    dict_col[board[i][j]] += 1
                    if dict_col[board[i][j]] > 1:
                        return False
        for p in range(0, 7, 3):
            for q in range(0, 7, 3):
                dict_cell = defaultdict(int)
                for i in range(p, p + 3):
                    for j in range(q, q + 3):
                        if board[i][j] != '.':
                            dict_cell[board[i][j]] += 1
                            if dict_cell[board[i][j]] > 1:
                                return False
        return True
    
#faster than 73.92%, memory less than 63.74%