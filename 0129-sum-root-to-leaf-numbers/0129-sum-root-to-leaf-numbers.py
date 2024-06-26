# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        res = []
        def trav(r,s):
            if not r:
                return
            if not r.left and not r.right:
                res.append(s + str(r.val))
            trav(r.left, s + str(r.val))
            trav(r.right, s + str(r.val))
        
        trav(root,'')
        res = [int(x) for x in res]
        res = sum(res)
        return res
            
            
        