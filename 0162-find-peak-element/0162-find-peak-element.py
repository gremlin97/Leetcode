class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        for i in range(len(nums)-1):
            if nums[i+1] < nums[i]:
                return i
        return len(nums)-1
    
                
        
                
                
                
                
        