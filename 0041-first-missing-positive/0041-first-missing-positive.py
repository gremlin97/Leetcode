class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        s = set()
        for x in nums:
            if x>0:
                s.add(x)
            
        for i in range(1, len(s) + 2):
            if i not in s:
                return i 

        
        