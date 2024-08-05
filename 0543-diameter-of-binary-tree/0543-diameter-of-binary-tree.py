# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0
        def dfs(r):
            if not r:
                return 0
            
            lh = dfs(r.left)
            rh = dfs(r.right)
            
            nonlocal res
            res = max(res, lh+rh)
            
            return 1 + max(lh, rh)
        
        dfs(root)
        return res