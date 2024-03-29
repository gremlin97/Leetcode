# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        res = []

        def search(r, v):
            if r is None:
                return None
            elif r.val == v:
                return r
            elif v<r.val:
                return search(r.left, v)
            else:
                return search(r.right, v)
        
        return search(root, val)
        
            