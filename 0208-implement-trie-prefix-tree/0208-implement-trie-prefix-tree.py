class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False
    
class Trie:

    def __init__(self):
        self.node = TrieNode()
    
    def insert(self, word: str) -> None:
        n = self.node
        for c in word:
            if c not in n.children:
                n.children[c] = TrieNode()
            n = n.children[c]
        n.end = True
                
        
    def search(self, word: str) -> bool:
        n = self.node
        for c in word:
            if c not in n.children:
                return False
            else:
                n = n.children[c]
        return n.end


    def startsWith(self, prefix: str) -> bool:
        n = self.node
        for c in prefix:
            if c not in n.children:
                return False
            else:
                n = n.children[c]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)