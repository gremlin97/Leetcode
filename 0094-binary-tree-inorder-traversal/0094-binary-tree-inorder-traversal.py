# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        myList= []
        if not root:
            return []
        self.traverse(myList, root)
        return myList
        
    def traverse(self, a, root):
        if(root.left == None):
            a.append(root.val)
        elif(root.left != None):
            self.traverse(a, root.left)
            a.append(root.val)
        if(root.right == None):
            return
        else:
             self.traverse(a, root.right)
        return

    
    
            
        


            
        