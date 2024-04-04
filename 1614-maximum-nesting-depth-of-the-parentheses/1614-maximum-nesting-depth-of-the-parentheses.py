class Solution:
    def maxDepth(self, s: str) -> int:
        # if s == '':
        #     return 0
        
        # if len(s) == 1:
        #     return 0
        
        stack = []
        count = 0
        mx_count = - float('inf')
        for x in s:
            print(count)
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
        