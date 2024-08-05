# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = -float('inf')
        
        def dfs(r):
            nonlocal res
            
            if not r:
                return 0
            
            ls = dfs(r.left)
            rs = dfs(r.right)
            
            res = max(res, ls+rs+r.val)
            
            return max(ls + r.val, rs + r.val, 0)
        
        dfs(root)
        return res
            
            
        