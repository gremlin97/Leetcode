class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        subs = []
        
        def recur(i):
            if i == len(nums):
                res.append(subs[::])
                return
            

            subs.append(nums[i])
            recur(i+1)
            
            subs.pop()
            
            while i<len(nums) - 1 and nums[i+1] == nums[i]:
                i += 1
            recur(i+1)
            
            return
        
        recur(0)
        return res
        