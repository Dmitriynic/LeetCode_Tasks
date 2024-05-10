# 125 Valid Palindrome

class Solution:
    def isPalindrome(self, s: str) -> bool:
        regex = re.compile('[^a-zA-Z0-9]+')
        s = regex.sub('', s)
        s = s.lower()
        len_ = len(s)
        count_ = 0
        if len_ % 2 == 1:
            count_ = 1
        if s[:len_//2] == s[len_-1:len_//2-1+count_:-1] or len_ == 0:
            return True
        else:
            return False

#faster than 93.37%, memory less than 21.24%
