class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = []
        right = []
        res = []
        
        prod = 1
        
        for x in nums:
            prod = prod * x
            left.append(prod)
        
        prod = 1
        
        for i in range(len(nums)-1, -1, -1):

            prod = prod * nums[i]
            right.append(prod)
            
        right.reverse()
        
        res.append(right[1])
        
        for i in range(1, len(nums)-1):
            temp = left[i-1]*right[i+1]
            res.append(temp)
        
        res.append(left[len(nums)-2])
        return res
        
        