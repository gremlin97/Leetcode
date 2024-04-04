class Solution:
    def maxDepth(self, s: str) -> int: 
        stack = []
        count = 0
        mx_count = - float('inf')
        for x in s:
            if x == '(':
                stack.append(x)
                count += 1
            elif x == ')':
                while stack[-1] != '(':
                    stack.pop()
                stack.pop()
                mx_count = max(mx_count, count)
                count -= 1
            else:
                stack.append(x)
        
        return max(0, mx_count)
        