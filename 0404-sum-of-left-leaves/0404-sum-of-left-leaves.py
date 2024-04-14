# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root or (not root.left and not root.right):
            return 0

        res = []
        
        def trav(r, l):
            if not r.left and not r.right and l == 1:
                res.append(r.val)
            if r.left:
                trav(r.left, 1)
            if r.right:
                trav(r.right, 0)
        
        trav(root, l=1)
        print(res)
        return sum(res)
                
        