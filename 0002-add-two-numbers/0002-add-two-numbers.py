# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def getdigits(head: str):
            res = ''
            curr = head
            
            while(curr != None):
                res += str(curr.val)
                curr = curr.next
            
            return res
        
        d1 = getdigits(l1)
        d1 = d1[::-1]
        d2 = getdigits(l2)
        d2= d2[::-1]
        
        print(d1, d2)
        s = list(str(int(d1) + int(d2)))
        s.reverse()
        
        head = ListNode(val = s[0]) 
        curr = head
        
        for i in range(1, len(s)):
            new = ListNode(val = s[i])
            curr.next = new
            curr = new
        
        return head
            
            
            
                
        
        