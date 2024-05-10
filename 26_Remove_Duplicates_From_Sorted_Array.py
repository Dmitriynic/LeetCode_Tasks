# 26 Remove Duplicates From Sorted Array

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        index = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[index - 1]:
                nums[index] = nums[i]
                index += 1
        return index

#faster than 40.44%, memory less than 23.96%
