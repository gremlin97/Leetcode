class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, total = 0, 0 
        res = float("inf")
        
        for r in range(0, len(nums)):
            print(l,r)
            total += nums[r]
            while total >= target:
                res = min(r - l + 1 , res)  
                total -= nums[l]
                l += 1
                
        if res == float('inf'):
            return 0
        return res
                    
        
                    
                
                
            
                
        
        