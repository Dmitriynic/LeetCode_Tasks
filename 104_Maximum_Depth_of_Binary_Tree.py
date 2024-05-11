#104 Maximum Depth of Binary Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def maxDepthCount(self, root: Optional[TreeNode]) -> int:
            if not root:
                return 0
            else:
                return max(maxDepthCount(self, root.left), maxDepthCount(self, root.right)) + 1
        return maxDepthCount(self, root)

#36ms faster than 79.70%, memory 17.6MB less than 50.50%
