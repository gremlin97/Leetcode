# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    res = 0
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def recur(r):
            if not r:
                return 0
            
            l = recur(r.left) + 1
            r = recur(r.right) + 1
            
            self.res = max(self.res, l + r - 2)
            
            return max(l, r)
        
        recur(root)
        return self.res