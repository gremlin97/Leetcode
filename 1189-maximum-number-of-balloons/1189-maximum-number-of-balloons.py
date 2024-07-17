class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        check = ['b','a','l','o','n']
        d = {}
        
        for x in text:
            if x in check:
                if x not in d:
                    if x!='l' and x!='o':
                        d[x] = 1
                    else:
                        d[x] = 1/2
                elif x in d:
                    if x!='l' and x!='o':
                        d[x] += 1
                    else:
                        d[x] += 1/2

        if sorted(list(d.keys())) == sorted(check):
            return int(min(d.values()))
        return 0
                        
            
        