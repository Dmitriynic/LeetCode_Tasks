#200_Number_of_Islands
 
def func_(grid, i, j):
    if grid[i][j] == '1':
        grid[i][j] = '2'
        if i != 0:
            func_(grid, i - 1, j)
        if j != 0:
            func_(grid, i, j - 1)
        if i != len(grid) - 1:
            func_(grid, i + 1, j)
        if j != len(grid[0]) - 1:
            func_(grid, i, j + 1)

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    func_(grid, i, j)
                    ans += 1
        return ans

#faser than 97.30%, memory less than 97.72%
