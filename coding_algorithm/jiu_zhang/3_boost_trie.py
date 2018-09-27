class ConnectingGraph:
    """
    @param: n: An integer
    """
    def __init__(self, n):
        # do intialization if necessary
        self.father = {}
        for i in range(n + 1):
            self.father[i] = i

    def find(self, father, node):
        path = []
        while node != father[node]:
            path.append(node)
            node = father[node]
        for n in path:
            father[n] = node
        return node
    
    def union(self, a, b):
        a_father = self.find(self.father, a)
        b_father = self.find(self.father, b)
        self.father[a_father] = b_father

    def connect(self, a, b):
        self.union(a, b)

    # find if a and b have same father,
    def query(self, a, b):
        print(self.father)
        if self.find(self.father, a) == self.find(self.father, b):
            return True
        return False


test = ConnectingGraph(4)
# [query(0,2),modify(0,4),query(0,1),modify(2,1),query(2,4)]
r = test.query(0, 2)
print(r)
r = test.query(1, 2)
print(r)
r = test.connect(1, 2)
print(r)
r = test.query(1, 3) # return false
print(r)
r = test.connect(2, 4)
print(r)
r = test.query(1, 4) # return true
print(r)
print(test.father)

class TrieNode():
    def __init__(self,):
        self.childern = {}
        self.is_word = False

class Trie:
    
    def __init__(self):
        # do intialization if necessary
        self.trie = TrieNode()

    """
    @param: word: a word
    @return: nothing
    """
    def insert(self, word):
        node = self.trie
        for c in word:
            if c not in node.childern:
                node.childern[c] = TrieNode()
            node = node.childern[c]
        node.is_word = True

    """
    @param: word: A string
    @return: if the word is in the trie.
    """
    def search(self, word):
        node = self.trie
        for c in word:
            if c not in node.childern:
                return False
            node = node.childern[c]
        if node.is_word:
            return True
        return False

    """
    @param: prefix: A string
    @return: if there is any word in the trie that starts with the given prefix.
    """
    def startsWith(self, prefix):
        node = self.trie
        for c in prefix:
            if c not in node.childern:
                return False
            node = node.childern[c]
        return True

test = Trie()
r = test.insert("lintcode")
print(test.trie.childern)
r = test.search("code")
print(r)
r = test.startsWith("lint")
print(r)
# true
r = test.startsWith("linterror")
print(r)
# false
r = test.insert("linterror")
r = test.search("lintcode")
print(r)
# true
r = test.startsWith("linterror")
print(r)
# true
