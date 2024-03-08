class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = []
        right = []
        res = []
        
        p = 1
        for i in range(len(nums)):
            p *= nums[i]
            left.append(p)
            
        p = 1
        for i in range(len(nums) - 1 ,-1,-1):
            p *= nums[i]
            right.append(p)
        right.reverse()
        
        
        res.append(right[1])
        for i in range(1,len(nums)-1):
            res.append(left[i-1]*right[i+1])

        res.append(left[len(nums)-2])
        return res
            
            
        
        