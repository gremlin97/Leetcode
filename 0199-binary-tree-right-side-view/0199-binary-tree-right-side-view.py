# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return None
        
        res = []
        
        q = []
        q.append(root)
        
        trav = []
        
        while q:
            temp = []
            for _ in range(len(q)):
                n = q.pop(0)
                
                temp.append(n.val)
                
                if n.left:
                    q.append(n.left)
                
                if n.right:
                    q.append(n.right)
                    
                
            trav.append(temp)
        
        print(trav)
        
        for r in trav:
            res.append(r[-1])
        
        return res
            
                    
            
                
            
            
            
        