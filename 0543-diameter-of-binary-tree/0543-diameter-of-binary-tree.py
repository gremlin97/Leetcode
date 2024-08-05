# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        def height(r):
            if not r:
                return 0
            return 1 + max(height(r.left), height(r.right))
        
        def diameter(r):
            if not r:
                return 0
            hl = height(r.left)
            hr = height(r.right)
            
            ld = diameter(r.left)
            rd = diameter(r.right)
            
            return max(hl+hr+1, max(ld,rd))
        
        return diameter(root)-1
            
        
        