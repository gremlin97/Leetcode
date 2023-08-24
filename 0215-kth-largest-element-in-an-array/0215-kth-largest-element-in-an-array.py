class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        print(nums)
        return nums[len(nums)-1-(k-1)]
        