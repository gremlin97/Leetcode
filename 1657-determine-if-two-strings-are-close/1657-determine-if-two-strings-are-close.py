class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        return (Counter(list(Counter(word1).values())) ==  Counter(Counter(word2).values()) and set(word1) == set(word2))
        