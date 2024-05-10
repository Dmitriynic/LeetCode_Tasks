#169 Majority Element

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        const_ = len(nums) / 2
        vote = 0
        ans = nums[0]
        for elem in nums:
            if elem == ans:
                vote += 1
            else:
                vote -= 1
            if vote < 0:
                vote = 1
                ans = elem
            if vote > const_:
                break
        return ans

#faster than 74.42%, memory less than 78.50%
