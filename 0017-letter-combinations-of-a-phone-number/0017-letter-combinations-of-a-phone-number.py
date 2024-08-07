class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        d = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
        
        def recur(i, curr):
            if len(curr) == len(digits):
                res.append(curr)
                return
            
            for x in d[digits[i]]:
                curr += x 
                recur(i+1, curr)
                curr = curr[:len(curr)-1]
            
        if not digits:
            return []
        recur(0, '')
        return res
        