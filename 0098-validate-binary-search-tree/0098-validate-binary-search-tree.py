# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        trav = []
        
        def inorder(r):
            if not r:
                return
            
            inorder(r.left)
            trav.append(r.val)
            inorder(r.right)
            
        inorder(root)
        
        print(trav, set(trav))
        if len(trav)!= len(set(trav)):
            return False
        return trav == sorted(trav)
        