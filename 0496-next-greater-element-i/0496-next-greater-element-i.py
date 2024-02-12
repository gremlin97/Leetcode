class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        order = [-1] * len(nums2)
        stack = []
        res = []
        
        for i, v in enumerate(nums2):
            while stack and v>stack[-1][1]:
                si, sv = stack.pop()
                order[si] = v
            stack.append([i,v])
        
        print(order, stack)
        
        for x in nums1:
            res.append(order[nums2.index(x)])
        
        return res
                
                
        