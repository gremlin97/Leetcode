class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        nums.sort()
        for x in nums:
            if x<0:
                if -x in nums:
                    return -x
            else:
                return -1
        
        return -1