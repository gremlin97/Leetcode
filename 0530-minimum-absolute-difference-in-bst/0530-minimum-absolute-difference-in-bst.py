# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        trav = []
        m = float('inf')
        
        def inorder(r):
            if not r:
                return
            
            inorder(r.left)
            trav.append(r.val)
            inorder(r.right)

        inorder(root)
        
        for i in range(0, len(trav)-1):
            diff = trav[i+1] - trav[i]
            if diff<m:
                m = diff
        
        return m