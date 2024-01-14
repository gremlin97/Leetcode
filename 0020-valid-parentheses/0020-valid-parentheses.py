class Solution:
    def isValid(self, s: str) -> bool:
        hashmap = {')':'(','}':'{',']':'['}
        
        stack = []
        
        for x in s:
            if x not in hashmap:
                stack.append(x)
            else:
                if stack and stack[-1] == hashmap[x]:
                        stack.pop()
                else:
                    return False
        
        if stack:
            return False
        return True
        