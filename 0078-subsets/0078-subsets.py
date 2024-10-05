class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subs = []
        
        
        def recur(i):
            if i == len(nums):
                res.append(subs[::])
                return
            
            subs.append(nums[i])
            recur(i+1)
            
            subs.pop()
            recur(i+1)
            
            return 
        
        recur(0)
        return res
            