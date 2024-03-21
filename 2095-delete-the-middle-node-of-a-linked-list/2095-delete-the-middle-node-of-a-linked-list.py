# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next == None:
            return None
        
        curr = head
        n = 0
        while(curr != None):
            curr = curr.next
            n+=1

        curr = head
        i = 0 
        while(i != n//2):
            i+=1
            prev = curr
            curr = curr.next
        
        curr = curr.next
        prev.next = curr
        return head
            
        
            
        
        