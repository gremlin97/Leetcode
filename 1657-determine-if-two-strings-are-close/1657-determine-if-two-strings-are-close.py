class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        return (sorted(word1) == sorted(word2)) or (set(word1) == set(word2) and Counter(Counter(word1).values()) == Counter(Counter(word2).values()))
        