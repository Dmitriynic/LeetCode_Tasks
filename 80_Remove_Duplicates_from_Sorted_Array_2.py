class Solution:
# 80 Remove Duplicates from Sorted Array 2

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        index = 1
        count_ = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[index - 1] and count_ < 2:
                nums[index] = nums[i]
                index += 1
                count_ += 1
            elif nums[i] != nums[index - 1]:
                nums[index] = nums[i]
                index += 1
                count_ = 1
        return index

#faster than 42.67%, memory less than 25.04%
