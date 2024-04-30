# 5 Longest Palindromic Substring

class Solution:
    def longestPalindrome(self, s: str) -> str:
        center = 0
        right = 0
        ans = s[0]
        while center < len(s) - 1:
            if center - right > -1 and center + right + 1 < len(s) and s[center - right] == s[center + right + 1]:
                if 2*right + 2 > len(ans):
                    ans = s[center - right:center+1] + s[center+1:center + right + 2]
                right += 1
            else:
                right = 0
                center += 1
        center = 0
        right = 1
        while center < len(s) - 1:
            if center - right > -1 and center + right < len(s) and s[center - right] == s[center + right]:
                if 2*right + 1 > len(ans):
                    ans = s[center - right:center] + s[center:center+right+1]
                right += 1
            else:
                right = 1
                center += 1
        return ans
            
#573ms faster than 46.41%, memory less than 50.43%