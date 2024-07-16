class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        l = 1
        r = 1
        mx = -float('inf')
        
        for i in range(len(nums)):
            l = l*nums[i]
            r = r*nums[len(nums)-1-i]
            mx = max(l,r,mx)
            if nums[i] == 0:
                l = 1
            if nums[len(nums)-i-1] == 0:
                r = 1
            
        return mx
        
        