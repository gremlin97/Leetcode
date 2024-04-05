class Solution:
    def makeGood(self, s: str) -> str:
        s = list(s)
        i = 0
        flag = False
        while i < (len(s) - 1):
            print(s)
            if s[i].lower() == s[i+1].lower() and s[i] != s[i+1]:
                s.pop(i)
                s.pop(i)
                flag = True
            i += 1
            if i >= len(s) - 1 and flag:
                i = 0
                flag = False
        return ''.join(s)
            
                
            
        