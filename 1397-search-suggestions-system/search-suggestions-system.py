from typing import List, Dict

class TrieNode:
    __slots__ = ("children", "suggestions")
    def __init__(self):
        self.children: Dict[str, TrieNode] = {}
        # Keep up to 3 lexicographically smallest words that pass through this node
        self.suggestions: List[str] = []

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
            # Because we'll insert words in sorted order, just append up to 3
            if len(node.suggestions) < 3:
                node.suggestions.append(word)

    def get_suggestions_for_prefixes(self, searchWord: str) -> List[List[str]]:
        res = []
        node = self.root
        for ch in searchWord:
            if node and ch in node.children:
                node = node.children[ch]
                res.append(node.suggestions)
            else:
                # Once a prefix path is missing, remaining prefixes have no matches
                node = None
                res.append([])
        return res

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()  # ensures lexicographic order for top-3 at each node
        trie = Trie()
        for w in products:
            trie.insert(w)
        return trie.get_suggestions_for_prefixes(searchWord)

        