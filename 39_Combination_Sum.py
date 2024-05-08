#39 Combination Sum

def func_(candidates, target, temp_arr, res):
    for elem in candidates:
        if not temp_arr or temp_arr[-1] <= elem:
            if sum(temp_arr) + elem == target:
                temp_arr.append(elem)
                res.append(temp_arr[:])
                temp_arr.pop()
            elif sum(temp_arr) + elem < target:
                temp_arr.append(elem)
                res = func_(candidates, target, temp_arr, res)
                temp_arr.pop()
            else:
                break
    return res
        
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        func_(candidates, target, [], res)
        return res
    
#faster than 85.89% memory less than 85.41%