# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        twin_sum = -float('inf')
        last = head
        first = head
        twin_list = []
        
        while last is not None:
            twin_list.append(last.val)
            last = last.next
        
        i = 0
        twin_list.reverse()
        print(twin_list)
        
        while first is not None:
            print(first.val, twin_list[i])
            twin_sum = max(twin_sum, (first.val + twin_list[i]))
            first = first.next
            i += 1
        
        return twin_sum
        
        
        