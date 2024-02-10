# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        trav = []
        q = []
        q.append(root)
        res = []
        
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
            
        
        for x in trav:
            res.append(x[len(x)-1])
            
        return res
            

        