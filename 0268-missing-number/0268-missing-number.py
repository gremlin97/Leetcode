class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = 0
        
        for x in nums:
            res = res ^ x
        
        for i in range(len(nums)+1):
            res = res ^ i
        
        return res
        