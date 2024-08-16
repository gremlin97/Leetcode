class Solution:
    def isPalindrome(self, s: str) -> bool:
        sc = []
        for x in s:
            if x.isalnum():
                sc.append(x.lower())
        
        if sc == sc[::-1]:
            return True
        return False
        