class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        curr = []
        
        def recur(curr):
            if len(curr) == len(nums):
                res.append(curr.copy())
                return
            
            for x in nums:
                if x not in curr:
                    curr.append(x)
                    recur(curr)
                    curr.pop()
        
        recur([])
        return res
                    
        