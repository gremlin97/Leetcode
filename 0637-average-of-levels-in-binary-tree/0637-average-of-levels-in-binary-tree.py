# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        trav = []
        q = []
        res = []
        
        q.append(root)
        
        while(q):
            temp = []
            for _ in range(0, len(q)):
                n = q.pop(0)
                temp.append(n.val)
                if n.left:
                    q.append(n.left)
                if n.right:
                    q.append(n.right)
            
            trav.append(temp)
            
        for x in trav:
            avg = sum(x)/len(x)
            res.append(avg)
        
        return res
            

        