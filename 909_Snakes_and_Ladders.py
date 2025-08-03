### 909 Snakes And Ladders

from collections import deque

class Solution:

    def snakesAndLadders(self, board):
        n = len(board)
        min_target = [-1] * (n * n)
        print(min_target)
        q = deque()
        min_target[1] = 0
        q.append(1)

        while q:
            curr = q.popleft()
            
            for k in range(curr + 1, curr + 7):
                if k > n * n:
                    break
                row = (k - 1) // n
                col = (k - 1) % n

                if row % 2 == 0:
                    v = board[n - 1 - row][col]
                else:
                    v = board[n - 1- row][n - 1 - col]
                
                if v > 0:
                    y = v
                else:
                    y = k
                
                if y == n * n:
                    return min_target[curr] + 1

                if min_target[y] == -1:
                    min_target[y] = min_target[curr] + 1
                    q.append(y)

        return -1

### Faster than 91,67%, lower mem than 92,52%