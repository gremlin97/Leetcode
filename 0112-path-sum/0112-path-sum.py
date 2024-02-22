# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        currSum = 0
        return self.psum(root, currSum, targetSum)
    
    def psum(self, r: TreeNode, currSum: int, targetSum: int):
        if not r:
            return
        
        currSum += r.val
        
        if (currSum == targetSum) and (not r.left and not r.right):
            return True
        
        if (currSum != targetSum) and (not r.left and not r.right):
            return False
        
        if r.left:
            if self.psum(r.left, currSum, targetSum):
                return True
            
        if r.right:
            if self.psum(r.right, currSum, targetSum):
                return True
            
        