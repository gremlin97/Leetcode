class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []
        
        def recur(c, o, stack):
            if c == o == n:
                res.append(''.join(stack))
                return res
            
            if o<n:
                stack.append('(')
                recur(c,o+1, stack)
                stack.pop()
            
            if c<o:
                stack.append(')')
                recur(c+1,o, stack)
                stack.pop()
                
        recur(0,0,stack)
        return res
        