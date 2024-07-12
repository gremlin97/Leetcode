# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        first = head
        last = head
        node_vals = []
        mx = -float('inf')
        
        while last:
            node_vals.append(last.val)
            last = last.next
        
        print(node_vals)
        i = 0
        while first:
            mx = max(mx, (first.val + node_vals[len(node_vals)-1-i]))
            first = first.next
            i += 1
            
        return mx
            
        
        
        