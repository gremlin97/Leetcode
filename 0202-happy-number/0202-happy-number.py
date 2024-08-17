class Solution:
    def isHappy(self, n: int) -> bool:
        visit = set()
        
        while n not in visit:
            visit.add(n)
            n = self.ss(n)
            
            if n == 1:
                return True
        return False
        
    def ss(self, n):
        s = 0
        while n:
            d = n%10
            s += d**2
            n = n//10
        return s
            
        