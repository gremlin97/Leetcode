# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = []
        res =[]
        
        if not root:
            return []
    
        q.append(root)
        
        while(q):
            temp = []
            for _ in range(len(q)):
                node = q.pop(0)
                temp.append(node.val)
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                
            res.append(temp)
        return res
                
            
        
