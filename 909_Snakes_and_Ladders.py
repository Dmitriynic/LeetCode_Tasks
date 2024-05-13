#909 Snakes and Ladders

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        maxnum = len(board) ** 2

        n = 0
        graph = [None] * (maxnum + 6)
        for i, row in enumerate(reversed(board)):
            for el in row[::-1 if i % 2 else 1]:
                n += 1
                if el > 0:
                    graph[n] = el

        curset , nextset = {1}, set()
        visited = {1}
        cntr = 0

        while curset and maxnum not in curset:
            for num in curset:
                for next_num in range(num + 1, num + 7):
                    if graph[next_num]:
                        next_num = graph[next_num]
                    if next_num not in visited:
                        nextset.add(next_num)
                        visited.add(next_num)
            
            curset.clear()
            curset, nextset = nextset, curset
            cntr += 1
 
        return  cntr if curset else -1

#82ms faster than 97.62%, 16.8MB memory less than 37.71%
