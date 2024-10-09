class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l = min(len(word1), len(word2))
        res = ''
        for i in range(l):
            res += word1[i]
            res += word2[i]
        print(res)
        if len(word1) > len(word2):
            
            res += word1[l:]
        else:
            res += word2[l:]
        return res