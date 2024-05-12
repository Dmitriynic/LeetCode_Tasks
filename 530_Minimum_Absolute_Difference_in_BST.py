# 530 Minimum Absolute Difference in BST

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def func_(root: Optional[TreeNode], prev_val):
    if root.left:
        func_(root.left, root.val)
    arr.append(root.val)
    if root.right:
        func_(root.right, root.val)
        
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        global arr
        arr = []
        min_ = inf
        func_(root, inf)
        for i in range(1, len(arr)):
            if abs(arr[i-1] - arr[i]) < min_:
                min_ = abs(arr[i-1] - arr[i])
        return min_
        
#46ms faster than 66.52%, 18.2MB memory less than 71.33%
