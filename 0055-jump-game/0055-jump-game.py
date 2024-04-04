class Solution:
    def canJump(self, nums: List[int]) -> bool:
        gas = 0
        for x in nums:
            if gas < 0:
                return False
            else:
                if gas<x:
                    gas = x
                gas -= 1
        
        return True
                
        