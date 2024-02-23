# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        q = []
        q.append(root)
        trav = []
        while q:
            for _ in range(len(q)):
                v = q.pop(0)
                trav.append(v.val)
                if v.left:
                    q.append(v.left)
                if v.right:    
                    q.append(v.right)
            
        return len(trav)
            
        