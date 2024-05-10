# 88 Merge Sorted Array

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        first = 0
        second = 0
        len_ind = len(nums1) - 1
        while m > 0 and n > 0:
            if nums1[m - 1] < nums2[n - 1]:
                nums1[len_ind] = nums2[n - 1]
                n -= 1
                len_ind -= 1
            else:
                nums1[len_ind] = nums1[m - 1]
                m -= 1
                len_ind -= 1
        while n > 0:
            nums1[len_ind] = nums2[n - 1]
            n -= 1
            len_ind -= 1
        return nums1

#faster than 69.33% memory less than 78.25%
