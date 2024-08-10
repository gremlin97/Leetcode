# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        s1 = ''
        s2 = ''
        curr1 = l1
        curr2 = l2
        
        while curr1:
            s1 += str(curr1.val)
            curr1 = curr1.next
            
        while curr2:
            s2 += str(curr2.val)
            curr2 = curr2.next
            
        s1 = s1[::-1]
        s2 = s2[::-1]
            
        s3 = str(int(s1) + int(s2))
        print(s3)
        
        s3 = list(s3)
        
        head = ListNode(int(s3[len(s3)-1]))
        curr = head
        
        for i in range(len(s3)-2,-1,-1):
            curr.next = ListNode(int(s3[i]))
            curr = curr.next
        
        return head
            
            
        