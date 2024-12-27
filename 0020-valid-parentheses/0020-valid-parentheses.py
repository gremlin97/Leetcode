class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        d = {")":"(", "]":"[", "}":"{"}
        
        for x in s:
            if not stack:
                stack.append(x)
            elif x not in d:
                stack.append(x)
            else:
                top = stack[-1]
                if d[x] == top:
                    stack.pop()
                else:
                    stack.append(x)
        
        if not stack:
            return True
        return False
        
        