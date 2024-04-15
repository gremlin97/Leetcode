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
            if not r.left and not r.right:
                res.append(s+str(r.val))
            if r.left:
                trav(r.left, s+str(r.val))
            if r.right:
                trav(r.right, s+str(r.val))
        
        trav(root,'')
        res = [int(x) for x in res]
        res = sum(res)
        print(res)
        return res
            
            
        