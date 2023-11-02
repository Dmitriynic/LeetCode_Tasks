#17. Letter combinations of a Phone Number
class Solution:
    list_ = {
        '2': "abc",
        '3': "def",
        '4': "ghi",
        '5': "jkl",
        '6': "mno",
        '7': "pqrs",
        '8': "tuv",
        '9': "wxyz"
    }
    def letterCombinations(self, digits: str) -> List[str]:
        arr = []
        if not digits:
            return None
        if len(digits) == 1:
            return list(self.list_[digits])
        arr = list(self.list_[digits[len(digits) - 1]])
        for i in range(len(digits) - 2, -1, -1):
            len_ = len(arr)
            arr1 = arr.copy()
            for j in range(len(self.list_[digits[i]]) - 1):
                arr += arr1
            q = 0
            for char_ in Solution.list_[digits[i]]:
                for l in range(len_):
                    arr[q] = char_ + arr[q]
                    q += 1
        return arr

##Runtime: 38 ms, faster than 57.58% of Python3 online submissions for Letter Combinations of a Phone Number.
#Memory Usage: 16.3 MB, less than 61.61% of Python3 online submissions for Letter Combinations of a Phone Number.
