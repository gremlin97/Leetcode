class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        f = float('inf')
        s = float('inf')
        
        for i in range(len(nums)):
            if nums[i] <= f:
                f = nums[i]
            elif nums[i] <= s:
                s = nums[i]
            else:
                return True
            
        return False
              
            
                
                
        