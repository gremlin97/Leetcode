# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        return self.psum(root, targetSum)
    
    def psum(self, r: TreeNode, targetSum: int):
        if not r:
            return False
        
        targetSum -= r.val
        
        if not r.left and not r.right:
            return targetSum == 0
 
        return (self.psum(r.left, targetSum) or (self.psum(r.right, targetSum)))
            
        