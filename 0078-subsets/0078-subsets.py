class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        
        def recur(i):
            
            if i == len(nums):
                res.append(subset.copy())
                return
            
            subset.append(nums[i])
            recur(i+1)
            
            subset.pop()
            recur(i+1)
        
        recur(0)
        return res
        