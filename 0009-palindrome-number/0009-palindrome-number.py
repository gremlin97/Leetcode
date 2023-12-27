class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = list(str(x))
        l = 0
        r = len(x) - 1 
        
        f = True
        
        while l<r:
            if x[l] != x[r]:
                f = False
                break
            l+=1
            r-=1
            
        return f
            