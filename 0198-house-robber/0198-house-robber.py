class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {-1:0, 0:nums[0]}
        
        for i in range(1, len(nums)):
            memo[i] = max(memo[i-1], memo[i-2] + nums[i])
        
        return memo[len(nums)-1]
        