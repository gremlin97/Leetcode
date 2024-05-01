class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        idx = word.find(ch)
        if ch == -1:
            return word
        word = word[:idx+1][::-1] + word[idx+1:]
        return word 
                
        