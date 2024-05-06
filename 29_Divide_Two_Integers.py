#29 Divide Two Integers

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        sign = 1
        if dividend < 0:
            dividend = -dividend
            sign *= -1
        if divisor < 0:
            divisor = -divisor
            sign *= -1
        plus_limit = 2 ** 31 - 1
        minus_limit = -(2 ** 31)
        result = len(range(0, dividend-divisor+1, divisor))
        result = min(max(sign*result, minus_limit), plus_limit)
        return result
    
#faster than 83.32% memory less than 75.19%