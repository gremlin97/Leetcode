class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        org = len(nums)
        _org = len(set(nums))
        
        if org - _org != 0:
            return True
        