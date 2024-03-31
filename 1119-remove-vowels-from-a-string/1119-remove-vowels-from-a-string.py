class Solution:
    def removeVowels(self, s: str) -> str:
        vowels = {'a','e','i','o','u'}
        s = list(s)
        i = 0
        while(i < len(s)):
            if s[i] in vowels:
                s.pop(i)
                i -= 1
            i+=1
        return ''.join(s)
        