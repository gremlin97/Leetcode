class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
            
        for i in range(0, len(nums)):
            if i>0 and i<len(nums)-1:
                print(i)
                if (nums[i] > nums[i-1] and nums[i] > nums[i+1]):
                    return i
            elif i==0:
                if nums[i]>nums[i+1]:
                    return 0
            else:
                if nums[i]>nums[i-1]:
                    return len(nums)-1
                
                
        