class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        curr = []
        nums.sort()
        
        def recur(i):
            if i == len(nums):
                res.append(curr.copy())
                return
            
            curr.append(nums[i])
            recur(i+1)
            
            curr.pop()
            
            while i<len(nums)-1 and nums[i] == nums[i+1]:
                i+=1
            recur(i+1)
        
        recur(0)
        return res
            
            
            