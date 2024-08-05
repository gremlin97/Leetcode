# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        trav = []
        def inorder(r):
            if not r:
                return
            inorder(r.left)
            trav.append(r.val)
            inorder(r.right)
        
        inorder(root)
        print(trav)
        return trav[k-1]
        