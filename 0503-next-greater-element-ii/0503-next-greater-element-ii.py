class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        res = [-1] * len(nums)
        
        for i,v in enumerate(2*nums):
            while stack and stack[-1][1] < v:
                stackI, stackV = stack.pop()
                res[stackI] = v
            stack.append([i%len(nums), v])
        return res
                
                
        