# 189 Rotate Array

def reverse(nums: List[int], i: int, j:int) -> None:
    while i < j:
        nums[i], nums[j] = nums[j], nums[i]
        i += 1
        j -= 1

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n
        reverse(nums, n - k, n - 1)
        reverse(nums, 0, n - k - 1)
        reverse(nums, 0, n - 1)

#faster than 48.78%, memory less than 10.11%
