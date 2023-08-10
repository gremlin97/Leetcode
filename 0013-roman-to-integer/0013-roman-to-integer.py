class Solution:
    def romanToInt(self, s: str) -> int:
        res = 0
        hashMap = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000, 'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}
        num = list(s)
        i = len(num)-1
        while i>=1:
            if num[i] == 'I':
                res += hashMap['I']
                i -= 1
                print('a')
                continue
                
            if num[i-1] + num[i] in hashMap:
                res += hashMap[num[i-1] + num[i]]
                i -= 2
                print('b')
            else:
                res += hashMap[num[i]]
                i -=1
                print('c')
        
        if i == 0:
            res += hashMap[num[i]]
        
        return res
            
            
                    
                    
                
            
        