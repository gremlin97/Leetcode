class Solution:
    def rob(self, nums: List[int]) -> int:
        @lru_cache(None)
        def prof(i):
            if i<0:
                return 0
            elif i == 0:
                return nums[0]
            else:
                return max(prof(i-2)+nums[i], prof(i-1))
        
        return prof(len(nums)-1)