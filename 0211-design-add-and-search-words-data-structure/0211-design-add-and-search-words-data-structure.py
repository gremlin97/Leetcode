class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False
        
class WordDictionary:

    def __init__(self):
        self.trie = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.trie
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.end = True
                
    def search(self, word: str) -> bool:
        node = self.trie
        return self.dfs(word, node)
        
    
    def dfs(self, word: str, node: TrieNode) -> bool:
        for i in range(len(word)):
            if word[i] == '.':
                curr = False
                for k in node.children.keys():
                    curr = curr or self.dfs(word[i+1:], node.children[k])
                if curr:
                    return True
                return False
            elif word[i] not in node.children:
                return False
            else:
                node = node.children[word[i]]
        return node.end

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)