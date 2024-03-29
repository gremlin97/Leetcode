# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        
        odd =  head
        even = head.next
        even_head = even
        
        while odd.next is not None and even.next is not None:
            odd_p = odd
            odd = odd.next.next
            
            even_p = even
            even = even.next.next
            
            odd_p.next = odd
            even_p.next = even
        
        odd.next = even_head
        return head
        
            
        