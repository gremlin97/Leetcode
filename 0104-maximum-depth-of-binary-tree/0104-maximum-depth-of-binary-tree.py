# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        def depth(a):
            
            if not a:
                return 0
            
            l = depth(a.left)
            r = depth(a.right)
            
            if l>=r:
                return l+1
            else:
                return r+1
        
        return depth(root)