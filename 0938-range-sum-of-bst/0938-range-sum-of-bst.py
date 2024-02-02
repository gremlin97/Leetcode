# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        trav, s = [], 0
        
        def inorder(r):
            
            if not r:
                return 
            
            inorder(r.left)
            trav.append(r.val)
            inorder(r.right)
            
        inorder(root)
        
        f = False
        
        for i in range(0, len(trav)):
            if low == trav[i]:
                f = True 
            
            if f:
                s += trav[i]
                
            if high == trav[i]:
                break
                
        
        return s
            
            
        
            
        