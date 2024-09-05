class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        curr = []
        
        def recur(o, c):
            if o == c == n:
                res.append(''.join(curr))
                return
            
            if o<n:
                curr.append('(')
                recur(o+1, c)
                curr.pop()
            
            if c<o:
                curr.append(')')
                recur(o, c+1)
                curr.pop()
        
        recur(0,0)
        return res