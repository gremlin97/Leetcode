# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def same(p, q):
            if not p and not q:
                return True
            if not p or not q:
                return False
            if p.val == q.val:
                return same(p.left, q.left) and same(p.right, q.right)
            
        def dfs(root):
            if not root:
                return
            if same(root, subRoot):
                return True
            if dfs(root.left) or dfs(root.right):
                return True
            return False
        
        return dfs(root)
            
            
            