class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {0:nums[0]}
        
        def r(i):
            if i<0:
                return 0
            elif i in memo:
                return memo[i]
            else:
                memo[i] = max(nums[i]+r(i-2), r(i-1))
                return memo[i]
            
        return r(len(nums)-1)
        