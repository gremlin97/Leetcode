# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        
        slow = head
        fast = head.next
        
        while fast is not None:
            slow = slow.next
            fast = fast.next
            
            if fast:
                fast = fast.next
            
            if slow == fast:
                return True
            
        return False
            
        