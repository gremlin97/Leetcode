class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {-1:0, 0:nums[0]}
        def prof(i):
            if i in memo:
                return memo[i]
            else:
                memo[i] = max(prof(i-2)+nums[i], prof(i-1))
                return memo[i]
        
        return prof(len(nums)-1)