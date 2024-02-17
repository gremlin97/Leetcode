class Solution:
    def fib(self, n: int) -> int:
        
        def fib_util(n):
            if n == 0:
                return 0
            elif n == 1:
                return 1
            else:
                return fib_util(n-1) + fib_util(n-2)
        
        return fib_util(n)
            
        