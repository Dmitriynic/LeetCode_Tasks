#6. zigzag convesion

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or len(s) <= numRows:
            return s
        rows = [[] for row in range(numRows)]
        index = 0
        step = -1
        for char in s:
            rows[index].append(char)
            if index == 0:
                step = 1
            elif index == numRows - 1:
                step = -1
            index += step
            
        for i in range(numRows):
            rows[i] = ''.join(rows[i])
        return ''.join(rows)
    
#faster than 39% and memory less than 72%