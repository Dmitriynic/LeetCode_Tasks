#34 Count and say
 
class Solution:
    def countAndSay(self, n: int) -> str:
        stri = "1"
        for i in range(1, n):
            count = 1
            ans = ""
            if len(stri) > 1:
                for j in range(1, len(stri)):
                    if stri[j-1] == stri[j]:
                        count += 1
                    else:
                        ans += str(count) + stri[j-1]
                        count = 1
                ans += str(count) + stri[j]
            else:
                ans += str(count) + stri
            count = 1
            stri = ans
        return stri

#faster than 75.62% memory less than 49.20%
