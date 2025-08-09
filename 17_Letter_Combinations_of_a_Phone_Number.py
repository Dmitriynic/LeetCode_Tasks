#17. Letter combinations of a Phone Number
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        dicti = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        out = [""]
        prev_out_len = 1

        if digits is None or len(digits) == 0:
            return []
        else:
            for i in range(len(digits) - 1, -1, -1):
                for j in range(1, len(dicti[digits[i]])):
                    for k in range(prev_out_len - 1, -1, -1):
                        out.append(dicti[digits[i]][j] + out[k])
                for k in range(prev_out_len - 1, -1, -1):
                    out[k] = dicti[digits[i]][0] + out[k]
                prev_out_len = len(out)
            return out

##Runtime: 0 ms, faster than 100% of Python3 online submissions for Letter Combinations of a Phone Number.
#Memory Usage: 12.17 MB, less than 99.97% of Python3 online submissions for Letter Combinations of a Phone Number.
