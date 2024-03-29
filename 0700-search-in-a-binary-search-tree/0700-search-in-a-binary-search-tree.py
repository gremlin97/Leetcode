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
                return
            elif r.val == v:
                res.append(r)
            elif v<r.val:
                search(r.left, v)
            else:
                search(r.right, v)
        
        search(root, val)
        if res == []:
            return None
        return res[0]
        
            