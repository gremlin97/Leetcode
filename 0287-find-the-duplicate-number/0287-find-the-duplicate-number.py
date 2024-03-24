class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        org = list(set(nums))
        s = set()
        for x in nums:
            if x in s:
                return x
            else:
                s.add(x)
        
