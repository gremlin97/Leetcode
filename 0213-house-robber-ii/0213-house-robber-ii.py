class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        l = len(nums)
        memo = {}
        def recur(i, nums):
            if i >= len(nums):
                return 0
            else:
                if i not in memo:
                    memo[i] = max((recur(i+2,nums) + nums[i]), recur(i+1,nums))
                    
                return memo[i]
        
        
        v1 = recur(0, nums[:len(nums)-1])
        memo.clear()
        v2 = recur(0, nums[1:])
        
        return max(v1,v2)