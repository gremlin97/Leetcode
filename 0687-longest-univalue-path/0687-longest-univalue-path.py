# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        res = 0
        def dfs(r):
            if not r:
                return 0
            
            l = dfs(r.left)
            ri = dfs(r.right)
            
            if r.left and r.val == r.left.val:
                l += 1
            else:
                l = 0
                
            if r.right and r.val == r.right.val:
                ri += 1
            else:
                ri = 0
            
            nonlocal res
            res = max(res, l + ri)
            return max(l,ri)
        
        dfs(root)
        return res