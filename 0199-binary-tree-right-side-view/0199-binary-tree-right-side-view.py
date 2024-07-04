# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = []
        q.append(root)
        trav = []
        
        if not root:
            return None
        
        while(q):
            temp = []
            for _ in range(len(q)):
                n = q.pop(0)
                temp.append(n.val)
                
                if n.left:
                    q.append(n.left)
                if n.right:
                    q.append(n.right)
                
            trav.append(temp)
        
        res = []
        for i in range(len(trav)):
            res.append(trav[i][len(trav[i])-1])
        return res
            
        