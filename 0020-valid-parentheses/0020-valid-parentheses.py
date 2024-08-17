class Solution:
    def isValid(self, s: str) -> bool:
        d = {')':'(',']':'[','}':'{'}
        stack = []
        
        for x in s:
            if x not in d:
                stack.append(x)
                continue            
            if stack and stack[-1] == d[x]:
                stack.pop()
            else:
                return False
        if stack:
            return False
        return True
        