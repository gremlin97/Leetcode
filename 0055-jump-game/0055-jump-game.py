class Solution:
    def canJump(self, nums: List[int]) -> bool:
        jump = nums[0]-1
        
        for i in range(1,len(nums)):
            if jump<0:
                return False
            elif nums[i] > jump:
                jump = nums[i]
                jump -= 1
            else:
                jump -= 1
        
        return True
        