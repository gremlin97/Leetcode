class Solution:
    def isPalindrome(self, x: int) -> bool:
        stack = []
        rev = []
        a = list(str(x))
        
        for v in a:
            stack.append(v)
        
        for v in a:
            e = stack.pop()
            rev.append(e)
            
        print(rev, a)
        return rev == a