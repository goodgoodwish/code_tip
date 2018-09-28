class TrieNode:
    def __init__(self,):
        self.child = {}
        self.is_word = False
class Solution:
    """
    @param: words: a set of words without duplicates
    @return: all word squares
    """
    def __init__(self,):
        self.root = TrieNode()
    def add(self, word):
        node = self.root
        for c in word:
            if c not in node.child:
                node.child[c] = TrieNode()
            node = node.child[c]
        node.is_word = True
    def search(self, word):
        node = self.root
        for c in word:
            if not in node.child:
                return False
            node = node.child[c]
        return node.is_word
    def wordSquares(self, words):
        results = []
        for word in words:
            if len(word) == 1:
                return words:
            self.add(word)
        for word in words:
            

        return results