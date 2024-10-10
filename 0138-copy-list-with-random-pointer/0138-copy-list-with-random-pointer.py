"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        a = head
        d = {None:None}
        
        while a:
            d[a] = Node(a.val)
            a = a.next
        
        curr = head
        
        while curr:
            copy = d[curr]
            copy.next = d[curr.next]
            copy.random = d[curr.random]
            curr = curr.next
            
        return d[head]

            
        
        
        