class Solution:
    def checkValidString(self, s: str) -> bool:
        brac = []
        star = []
        
        for i,c in enumerate(s):
            if c == '(':
                brac.append(i)
            elif c == ')':
                if brac:
                    brac.pop()
                elif star:
                    star.pop()
                else:
                    return False
            else:
                star.append(i)
        
        while(brac):
            if not star:
                return False
            elif brac[-1] < star[-1]:
                star.pop()
                brac.pop()
            else:
                return False
            
        return True
        
        
        