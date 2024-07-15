class Solution:
    def makeFancyString(self, s: str) -> str:
        stack = []
        for x in s:
            if len(stack)>=2 and x == stack[-1] == stack[-2]:
                stack.pop()
            stack.append(x)
        return ''.join(stack)
        