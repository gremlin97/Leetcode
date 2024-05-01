class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        x = 0
        for n in nums:
            x = x ^ n
        res = 0
        while x > 0 or k > 0:
            if x % 2 != k % 2:
                res += 1
            x = x >> 1
            k = k >> 1
        
        return res
            
        