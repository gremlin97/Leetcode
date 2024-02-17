class Solution:
    def fib(self, n: int) -> int:
        memo = {}
        
        def fib_util(n):
            if n == 0:
                return 0
            elif n == 1:
                return 1
            else:
                if n in memo.keys():
                    return memo[n]
                memo[n] = fib_util(n-1) + fib_util(n-2)
                return memo[n]
        
        return fib_util(n)
            
        