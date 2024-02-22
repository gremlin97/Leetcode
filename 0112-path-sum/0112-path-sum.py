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
        
        if (targetSum == 0) and (not r.left and not r.right):
            return True
        
        if (targetSum != 0) and (not r.left and not r.right):
            return False
        
        
        return (r.left and self.psum(r.left, targetSum) or (r.right and self.psum(r.right, targetSum)))
            
        