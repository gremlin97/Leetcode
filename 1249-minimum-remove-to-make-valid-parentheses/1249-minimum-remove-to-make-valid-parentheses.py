class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        remove = set()
        
        for i, c in enumerate(s):
            if c == '(':
                stack.append(i)
            elif c == ')':
                if stack:
                    stack.pop()
                else:
                    remove.add(i)
                    
        print(stack, remove)
        
        remove.update(stack)
        
        res = ''
        for i, c in enumerate(s):
            if i not in remove:
                res += c
        
        return res
                
        