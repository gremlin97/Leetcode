class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch in word:
            index = word.index(ch)
        else:
            return word
        f= ''
        s= ''
        for i in range(len(word)):
            if i<= index:
                f += word[i]
            else:
                s += word[i]
                
        res = f[::-1] + s
        return res
                
                
                
        