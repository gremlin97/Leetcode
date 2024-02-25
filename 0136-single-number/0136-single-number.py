class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        b = 0
        
        for x in nums:
            b = b  ^ x
            
        return b
        
    
    
        