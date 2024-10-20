class Solution:
    def reverse(self, x: int) -> int:
        res = 0 
        s = list(str(x))
        neg = False
        
        if x<0:
            s = s[1:]
            neg = True
            
        s.reverse()
        
        s = ''.join(s)
        s = int(s)
        
        if neg:
            s *= -1
        if s < -(2**(31)) or s > (2**31)-1: return 0
        return s
        