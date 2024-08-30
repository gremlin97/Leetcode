class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        a, b = 0, 0
        res = ''
        
        num1 = list(num1)
        num1.reverse()
        
        num2 = list(num2)
        num2.reverse()

        for i in range(len(num1)):
            a = a + (ord(num1[i])-48)*(10**i)
        
        for i in range(len(num2)):
            b = b + (ord(num2[i])-48)*(10**i)
        
        prod = a*b
        
        if prod == 0:
            return '0'
        
        while prod:
            dig = prod%10
            res = res + chr(dig + 48)
            prod = prod//10
        
        return res[::-1]
        
        
            
        