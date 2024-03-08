class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()
        print(s)
        s.reverse()
        s = " ".join(s)
        s = s.strip()
        return s