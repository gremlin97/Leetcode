class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {1:1, 2:2}
        def paths(n):
            if n in memo:
                return memo[n]
            else:
                memo[n] = paths(n-1) + paths(n-2) 
                return memo[n]
        
        return paths(n)
        