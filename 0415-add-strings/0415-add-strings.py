class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        res = []
        carry = 0
        a, b = list(num1), list(num2)
        
        while len(a)>0 or len(b)>0:
            if len(a)>0:
                d1 = ord(a.pop()) - ord('0')
            else:
                d1 = 0
            
            if len(b)>0:
                d2 = ord(b.pop()) - ord('0')
            else:
                d2 = 0
                
            val = d1 + d2 + carry
            carry = val//10
            add = val%10
            
            res.append(add)
        
        if carry>0:
            res.append(carry)
            
        res = res[::-1]
        res = [str(x) for x in res]
        return ''.join(res)
        