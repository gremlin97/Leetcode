# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def depth(r):
            if r is None:
                return 0

            l = depth(r.left) + 1
            r = depth(r.right) + 1

            return max(l, r)
    
        return depth(root)
        