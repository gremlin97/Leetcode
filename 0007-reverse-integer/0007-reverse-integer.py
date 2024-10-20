class Solution:
    def reverse(self, x: int) -> int:
        num = x
        res = 0
        neg = False
        size = len(str(x))-1
        if x < 0: 
            size -= 1
            num *= -1
            neg = True
            
        while num:
            # 123%10 = 3, num//10
            d = num%10
            num = num//10
            res = res + d*(10**(size))
            size -= 1
            if res > (2**31)-1 or res < -(2**31): return 0
            
            #print(num, d, res)
        
        
        if neg:
            return res*-1
        
        return res
            
        