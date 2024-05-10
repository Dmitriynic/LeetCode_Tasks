#209 Minimum Size Subarray Sum

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i = 0
        min_length = len(nums) + 1
        curr_length = 0
        curr_sum = 0
        while i < len(nums) or curr_sum >= target:
            if curr_sum < target:
                curr_sum += nums[i]
                i += 1
                curr_length += 1
            elif curr_sum >= target:
                if curr_length < min_length:
                    min_length = curr_length
                curr_sum -= nums[i - curr_length]
                curr_length -= 1
        if min_length == len(nums) + 1:
            return 0
        return min_length

#faster than 67.49%, memory less than 62.57%
