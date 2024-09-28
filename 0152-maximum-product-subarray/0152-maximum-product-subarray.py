class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        l = 1
        r = 1
        res = -float('inf')
        
        for i in range(len(nums)):
            l *= nums[i]
            r *= nums[len(nums)-1-i]
            
            res = max(l, r, res)
            
            if l == 0:
                l = 1
            if r == 0:
                r = 1
        
        return res
                
            
            
        
        