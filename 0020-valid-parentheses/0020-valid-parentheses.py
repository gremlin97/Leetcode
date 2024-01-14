class Solution:
    def isValid(self, s: str) -> bool:
        hashmap = {')':'(','}':'{',']':'['}
        
        stack = []
        
        for x in s:
            if x not in hashmap:
                stack.append(x)
            else:
                if stack:
                    print('Yes')
                    print(stack[-1], hashmap[x])
                    if stack[-1] == hashmap[x]:
                        stack.pop()
                    else:
                        return False
                else:
                    return False
        if len(stack)==0:
            return True
        return False
        