class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        l = 0
        r = l + k - 1
        max_s = s = sum(nums[l:r+1])
        
        while(r < (len(nums)) - 1):
            s = s + nums[r+1] - nums[l]
            max_s = max(s, max_s)
            l += 1
            r += 1
    
        return max_s/k