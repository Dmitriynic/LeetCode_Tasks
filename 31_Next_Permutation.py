#31 Next Permutation

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        i = len(nums) - 1
        if i != 0:
            if nums[i] > nums[i - 1]:
                nums[i], nums[i - 1] = nums[i - 1], nums[i]
            else:
                while nums[i] <= nums[i - 1] and i > 0:
                    i -= 1
                if i == 0:
                    return nums.sort()
                else:
                    res = nums[i:].index(min(filter(lambda x: x > nums[i - 1], nums[i:]))) + i
                    nums[i - 1], nums[res] = nums[res], nums[i - 1]
                    nums[i:] = sorted(nums[i:])
        return nums

#faster than 88.75%, memory less than 53.07%