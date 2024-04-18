# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        
        if depth == 1:
            temp = TreeNode(val)
            temp.left = root
            root = temp
            return root
        
        def insert(r, v, d):
            if not r:
                return
            
            d -= 1
            if d == 1:
                print(r.val)
                temp = r.left
                r.left = TreeNode(val)
                r.left.left = temp
                
                temp = r.right
                r.right = TreeNode(val)
                r.right.right = temp
                
                return
            
            insert(r.left, v, d)
            insert(r.right, v, d)
        
        insert(root, val, depth)
        return root
            
        