class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        for i in range(0, len(nums)):
            if sum(nums[0:i]) == sum(nums[i+1:len(nums)]):
                return i
        return -1
        