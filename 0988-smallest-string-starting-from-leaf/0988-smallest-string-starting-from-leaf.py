# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        
        trav = []
        def dfs(r,s):
            if not r:
                return
            if not r.left and not r.right:
                trav.append(chr(r.val+97) + s)
            dfs(r.left, chr(r.val+97) + s)
            dfs(r.right, chr(r.val+97) + s)
            
        dfs(root,'')
        trav.sort()
        return trav[0]
        