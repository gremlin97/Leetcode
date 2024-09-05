class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []
        
        def recur(c, o):
            if c == o == n:
                res.append(''.join(stack))
                return
            
            if o<n:
                stack.append('(')
                recur(c,o+1)
                stack.pop()
            
            if c<o:
                stack.append(')')
                recur(c+1,o)
                stack.pop()
                
        recur(0,0)
        return res