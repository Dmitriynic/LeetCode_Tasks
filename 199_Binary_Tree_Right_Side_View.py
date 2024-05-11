# 199 Binary Tree Right Side View

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque, defaultdict

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        deq = deque()
        dict_ = defaultdict()
        deq.append([root, 0])
        while deq:
            curr, lvl = deq.popleft()
            dict_[lvl] = curr.val
            if curr.left:
                deq.append([curr.left, lvl+1])
            if curr.right:
                deq.append([curr.right, lvl+1])
        return dict_.values()

#40ms faster than 29.07%, 16.6MB memory less than 7.96%
