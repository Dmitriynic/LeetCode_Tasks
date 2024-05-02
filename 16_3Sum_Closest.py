#3Sum_Closest

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        print(nums)
        left = 0
        right = len(nums) - 1
        mid = left + 1
        ans = nums[left] + nums[mid] + nums[right]
        diff = abs(ans - target)
        while mid < right:
            while mid < right:
                temp = nums[left] + nums[mid] + nums[right]
                temp_diff = abs(temp - target)
                if temp_diff == 0:
                    return temp
                if temp_diff < diff:
                    ans = temp
                    diff = temp_diff
                if temp < target:
                    mid += 1
                elif temp > target:
                    right -= 1
            left += 1
            mid = left + 1
            right = len(nums) - 1
        return ans
    
#faster than 75.49%, memory less than 59.33%