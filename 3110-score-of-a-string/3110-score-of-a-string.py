class Solution:
    def scoreOfString(self, s: str) -> int:
        t = 0
        for i in range(len(s)-1):
            t += abs(ord(s[i+1]) - ord(s[i]))
        return t
            
        