# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        res = []
        def encode(r):
            if not r:
                res.append('N')
                return
            
            res.append(str(r.val))
            encode(r.left)
            encode(r.right)
         
        encode(root)
        res = ','.join(res)
        print(res)
        return res

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        i = 0
        val = data.split(',')
        
        def decode():
            nonlocal i
            if val[i] == 'N':
                i += 1
                return None
            
            node = TreeNode(int(val[i]))
            i += 1
            node.left = decode()
            node.right = decode()
            return node
            
        return decode()
            

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))