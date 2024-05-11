# 228 Summary Ranges

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        if len(nums) == 1:
            return [f"{nums[0]}"]
        left = 0
        curr = 0
        ans = []
        while curr < len(nums):
            if nums[curr] - nums[left] > curr - left:
                if curr - left - 1 == 0:
                    ans.append(f"{nums[left]}")
                    left += 1
                    curr = left
                else:
                    ans.append(f"{nums[left]}->{nums[curr - 1]}")
                    left = curr
                    curr -= 1
            curr += 1
        if curr != left:
            if curr - left == 1:
                ans.append(f"{nums[left]}")
            else:
                ans.append(f"{nums[left]}->{nums[curr - 1]}")
        return ans

#24ms faster than 98.02%, memory 16.6MB less than 9.62%
