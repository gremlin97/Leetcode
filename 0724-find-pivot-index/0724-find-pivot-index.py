class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        for i in range(0, len(nums)):
            left_sum = sum(nums[0:i])
            right_sum = (total_sum - left_sum - nums[i])
            print(left_sum, right_sum)
            if left_sum == (total_sum - left_sum - nums[i]):
                return i
        return -1