# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        s1, s2 = l1, l2
        
        n1, n2 = '', ''
        
        
        while s1:
            n1 += str(s1.val)
            s1 = s1.next
        n1 = n1[::-1]
        
        
        while s2:
            n2 += str(s2.val)
            s2 = s2.next
        n2 = n2[::-1]
        
        
        add = str(int(n1) + int(n2))
        add = add[::-1]
        
        res = ListNode(add[0])
        head = res
        for x in add[1:]:
            res.next = ListNode(int(x))
            res = res.next
        return head
            
            
        
            
        
            
            
        