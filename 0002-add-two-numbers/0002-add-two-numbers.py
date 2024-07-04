# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # sum l1
        s1 = ''
        curr = l1
        while(curr):
            s1 += str(curr.val)
            curr = curr.next
        
        # sum l2
        s2 = ''
        curr = l2
        while(curr):
            s2 += str(curr.val)
            curr = curr.next
        
        s1 = int(s1[::-1])
        s2 = int(s2[::-1])
        
        s3 = str(s1 + s2)
        s3 = list(s3)
        s3.reverse()
        
        l3 = ListNode()
        l3.val = s3[0]
        
        # sum all
        curr = l3
        for i in range(1,len(s3)):
            temp = ListNode()
            temp.val = s3[i]
            temp.next = None
            
            curr.next = temp
            curr = curr.next
        
        return l3
        
        
            
        