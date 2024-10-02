# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    res = 0
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        
        def diameter(r):
            if not r:
                return 0
            
            le = diameter(r.left) + 1
            ri = diameter(r.right) + 1
            
            self.res = max(self.res, le + ri - 2)
            
            return max(le, ri)
        
        diameter(root)
        return self.res
        