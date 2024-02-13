class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        order = [-1] * len(nums)
        
        for i, v in enumerate(2*nums):
            while stack and v>stack[-1][1]:
                stackI, stackV = stack.pop()
                order[stackI] = v
            stack.append([i%len(nums), v])
        
        return order
        
        