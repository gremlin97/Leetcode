# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        res = []
        
        def trav(root):
            if root is None:
                return
            trav(root.left)
            if (root.left is None and root.right is None):
                res.append(root.val)
            trav(root.right)
        
        trav(root1)
        t1 = res
        res = []
        trav(root2)
        t2 = res
        return t1 == t2
        