# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        l1 = list1
        l2 = list2
        
        while l1 and l2:
            if l1.val < l2.val:
                curr.next = ListNode(l1.val)
                curr = curr.next
                l1 = l1.next
                continue
                
            if l1.val >= l2.val:
                curr.next = ListNode(l2.val)
                curr = curr.next
                l2 = l2.next
                
        
        if not l1:
            curr.next = l2
        if not l2:
            curr.next = l1
        
        return dummy.next
                
                
                
                
        