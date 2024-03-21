# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next == None:
            return None
        
        fast = head
        curr = head
        
        while(fast != None):
            if fast.next == None:
                break
            fast = fast.next
            fast = fast.next
            prev = curr
            curr = curr.next
        
        print(prev.val, curr.val)
        prev.next = curr.next
        return head
        
        
            
        
            
        
        