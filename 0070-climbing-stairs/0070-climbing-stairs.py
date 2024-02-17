class Solution:
    def climbStairs(self, n: int) -> int:
        memo = [-1] * (n+1)
        print(memo)
        
        def paths(n):
            if n<0:
                return 0
            if n == 0:
                return 1
            if memo[n] > 0:
                return memo[n]
            memo[n] = paths(n-1) + paths(n-2)
            return memo[n]
        
        return paths(n)
    
        