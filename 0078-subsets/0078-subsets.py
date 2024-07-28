class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subsets = []
        
        def recur(i):
            if i == len(nums):
                res.append(subsets.copy())
                return
            
            subsets.append(nums[i])
            recur(i+1)
            
            subsets.pop()
            recur(i+1)
        
        recur(0)
        return res