#22_Generate_Parentheses

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def func(left, right, s):
            if len(s)/2 == n:
                res.append(s)
                return None
            if left < n:
                func(left + 1, right, s + '(')
            if right < left:
                func(left, right+1, s + ')')
        res = []
        func(0, 0, '')
        return res
    
#faster than 79.77% memory less than 42.61%