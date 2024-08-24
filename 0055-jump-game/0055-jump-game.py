class Solution:
    def canJump(self, nums: List[int]) -> bool:
        jump = 0
        
        for x in nums:
            if jump<0:
                return False
            elif jump<x:
                jump = x
                jump -= 1
            else:
                jump -= 1
        
        return True