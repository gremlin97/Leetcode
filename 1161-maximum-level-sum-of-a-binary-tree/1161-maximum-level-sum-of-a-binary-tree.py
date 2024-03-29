# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        q = []
        q.append(root)
        trav = []
        
        while(q):
            temp = 0
            for _ in range(len(q)):
                n = q.pop(0)
                temp += n.val
                if n.left:
                    q.append(n.left)
                if n.right:
                    q.append(n.right)
            trav.append(temp)

        return (trav.index(max(trav)) + 1)
        