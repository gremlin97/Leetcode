class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        d = defaultdict(int)
        curr_sum = 0
        res = 0
        
        # 1 2 3 -  1 3 6 - 
        
        for i in range(len(nums)):
            curr_sum += nums[i]
            
            if curr_sum == k:
                res += 1
            
            if curr_sum - k in d:
                res += d[curr_sum - k]
            
            d[curr_sum] += 1
        
        return res
        