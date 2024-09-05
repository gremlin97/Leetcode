"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        d = {}
        
        def clone(n):
            if n.val not in d:
                curr = Node(n.val)
                d[n.val] = curr

                print(n.val)
                if n.neighbors:
                    for x in n.neighbors:
                        curr.neighbors.append(clone(x))
                return curr
            else:
                return d[n.val]
        
        res =  clone(node)
        return res

                
        