# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = []
        q.append(root)
        res = []
        
        if not root:
            return []
        while(q):
            temp = []
            for _ in range(0, len(q)):
                r = q.pop(0)
                temp.append(r.val)

                if r.left:
                    q.append(r.left)

                if r.right:
                    q.append(r.right)

            res.append(temp)
        
        return res    
            
