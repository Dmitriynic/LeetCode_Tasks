#9_Palindrome_Number

class Solution:
    def isPalindrome(self, x: int) -> bool:
        left = 0
        if x < 0:
            return False
        x = str(x)
        right = len(x) - 1
        ans = True
        if len(x) == 1:
            return ans
        while left < right:
            if x[left] != x[right]:
                ans = False
            left += 1
            right -= 1
        return ans

#faster than 87.33% memory less than 96.81%
