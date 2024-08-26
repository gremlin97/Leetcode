class Solution:
    def jump(self, nums: List[int]) -> int:
        l, r = 0, 0
        steps = 0
        max_jump = 0
        #2,3,1,1,4, l=r=0, 2, l=1, r=2
        while r<len(nums)-1:
            for i in range(l,r+1):
                max_jump = max(max_jump,nums[i] + i)
            l = r+1
            r = max_jump
            max_jump = 0
            steps += 1
        
        return steps
        
                
        