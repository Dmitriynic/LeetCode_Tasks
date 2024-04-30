#7_Reverse_Integer

class Solution:
    def reverse(self, x: int) -> int:
        str_x = str(x)
        if x >= 0:
            rev_str_x = str_x[::-1]
            if len(rev_str_x) > 10:
                return 0
            elif len(rev_str_x) == 10 and rev_str_x > str(2**31 - 1):
                return 0
            else:
                return int(rev_str_x)
        else:
            rev_str_x = str_x[:0:-1]
            if len(rev_str_x) > 10:
                return 0
            elif len(rev_str_x) == 10 and rev_str_x > str(2**31):
                return 0
            else:
                temp = int(rev_str_x)
                return temp * -1
            
#Faster than 96.23%, memory less than 68.96%
