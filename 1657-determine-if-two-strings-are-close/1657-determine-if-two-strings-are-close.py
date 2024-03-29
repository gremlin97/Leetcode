class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        return (sorted(word1) == sorted(word2)) or (sorted(list(Counter(word1).values())) ==  sorted(Counter(word2).values()) and set(word1) == set(word2))
        