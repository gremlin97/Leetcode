class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 1:
            return int(tokens[0])
        stack = []
        ops = ['+','-','/','*']
        
        for x in tokens:
            if x in ops:
                r = stack.pop()
                l = stack.pop()
                
                if x=='+':
                    exp = int(l)+int(r)
                    stack.append(exp)
                elif x=='-':
                    exp = int(l)-int(r)
                    stack.append(exp)
                elif x=='*':
                    exp = int(l)*int(r)
                    stack.append(exp)
                else:
                    exp = int(l)/int(r)
                    stack.append(exp)
            else:
                stack.append(x)

        return int(stack[-1])
                    
            
        