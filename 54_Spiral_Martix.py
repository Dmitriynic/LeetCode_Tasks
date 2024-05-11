# 54 Spiral Matrix

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n = len(matrix)
        m = len(matrix[0])
        i = 0
        j = 0
        ans = []
        ans.append(matrix[0][0])
        matrix[0][0] = -101
        while True:
            bool = False
            while j + 1 < m and matrix[i][j + 1] != -101:
                ans.append(matrix[i][j + 1])
                matrix[i][j + 1] = -101
                j += 1
                bool = True
            while i + 1 < n and matrix[i + 1][j] != -101:
                ans.append(matrix[i + 1][j])
                matrix[i + 1][j] = -101
                i += 1
                bool = True
            while j - 1 >= 0 and matrix[i][j - 1] != -101:
                ans.append(matrix[i][j - 1])
                matrix[i][j - 1] = -101
                j -= 1
                bool = True
            while i - 1 < n and matrix[i - 1][j] != -101:
                ans.append(matrix[i - 1][j])
                matrix[i - 1][j] = -101
                i -= 1
                bool = True
            if bool == False:
                break
        return ans

#faster than 73%, memory less than 60.51%
