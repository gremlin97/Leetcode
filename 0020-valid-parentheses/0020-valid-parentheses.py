class Solution:
    def isValid(self, s: str) -> bool:
        d = {')':'(', '}':'{', ']':'['}
        stack = []
    
        for x in s:
            if x not in d:
                stack.append(x)
            else:
                if stack and stack[-1] == d[x]:
                    stack.pop()
                else:
                    return False
        
        if not stack:
            return True
        else: return False

        