# 20 Valid Parentheses

class Solution:
    def isValid(self, s: str) -> bool:
        arr = []
        for elem in s:
            if elem == '(' or elem == '[' or elem == '{':
                arr.append(elem)
            elif elem == ')' and arr:
                if arr[-1] == '(':
                    arr.pop()
                else:
                    return False
            elif elem == ']' and arr:
                if arr[-1] == '[':
                    arr.pop()
                else:
                    return False
            elif elem == '}' and arr:
                if arr[-1] == '{':
                    arr.pop()
                else:
                    return False
            else:
                return False
        if not arr:
            return True
        else:
            return False

#40ms faster than 24.16%, memory 16.7MB less than 22.74%
