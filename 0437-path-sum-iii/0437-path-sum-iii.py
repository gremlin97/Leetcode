# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        res = 0
        
        def dfs(r, curr):
            nonlocal res
            if not r:
                return 
    
            curr.append(r.val)
            if sum(curr) == targetSum:
                res += 1
            
            temp = curr[::]
            
            dfs(r.left, curr)
            dfs(r.right, temp)
            
        def t(r):
            if not r:
                return

            dfs(r, [])
            t(r.left)
            t(r.right)
            
        t(root)
        
        return res
            
            
        