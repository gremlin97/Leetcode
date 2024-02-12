class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsum = nums[0]
        currsum = 0
        for i in range(len(nums)):
            currsum = max(currsum, 0)
            currsum += nums[i]
            maxsum = max(currsum, maxsum)
                
        return maxsum
                
                
                
        