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


class ConnectingGraph2:
    """
    @param: n: An integer
    """
    def __init__(self, n):
        self.father = {}
        self.size = {}
        for i in range(1, n + 1):
            self.father[i] = i
            self.size[i] = 1

    """
    @param: a: An integer
    @param: b: An integer
    @return: nothing
    """
    def connect(self, a, b):
        a_root = self.find(a)
        b_root = self.find(b)
        if a_root != b_root:
            self.father[a_root] = b_root
            self.size[b_root] += self.size[a_root]

    """
    @param: a: An integer
    @return: An integer
    """
    def query(self, a):
        return self.size[self.find(a)]
    def find(self, a):
        node = a
        path = []
        while self.father[node] != node:
            path.append(node)
            node = self.father[node]
        for n in path:
            self.father[n] = node
        return node

test = ConnectingGraph2(4)

r = test.query(1) # return 1
print(r)
r = test.connect(1, 2)
print(r)
r = test.query(1) # return 2
print(r)
r = test.connect(2, 4)
print(r)
r = test.query(1) # return 3
print(r)
r = test.connect(1, 4)
print(r)
r = test.query(1) # return 3
print(r)

class ConnectingGraph3:
    """
    @param a: An integer
    @param b: An integer
    @return: nothing
    """
    def __init__(self, n):
        self.father = {}
        self.count = n
        for i in range(1, n + 1):
            self.father[i] = i

    def connect(self, a, b):
        a_root = self.find(a)
        b_root = self.find(b)
        if a_root != b_root:
            self.father[a_root] = b_root
            self.count -= 1
    
    def find(self, a):
        path = []
        node = a
        while node != self.father[node]:
            path.append(node)
            node = self.father[node]
        for n in path:
            self.father[n] = node
        return node

    def query(self):
        return self.count

test = ConnectingGraph3(5)

r = test.query() # return 5
print(r)
test.connect(1, 2)
r = test.query() # return 4
print(r)
test.connect(2, 4)
r = test.query() # return 3
print(r)
test.connect(1, 4)
r = test.query() # return 3
print(r)


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

class TrieNode():
    def __init__(self,):
        self.char_child = {}
        self.is_word = False

class WordDictionary:
    """
    @param: word: Adds a word into the data structure.
    @return: nothing
    """
    def __init__(self,):
        self.root = TrieNode()

    def addWord(self, word):
        node = self.root
        for c in word:
            if c not in node.char_child:
                node.char_child[c] = TrieNode()
            node = node.char_child[c]
            print(c)
        node.is_word = True

    """
    @param: word: A word could contain the dot character '.' to represent any one letter.
    @return: if the word is in the data structure.
    """
    def search_char(self, word, node, index):
        if node is None:
            return False
        if len(word) == index:
            return node.is_word
        if word[index] == ".":
            for c in node.char_child:
                if self.search_char(word, node.char_child.get(c), index + 1):
                    return True
            return False
        return self.search_char(word, node.char_child.get(word[index]), index + 1)

    def search(self, word):
        return self.search_char(word, self.root, 0)


test = WordDictionary()

test.addWord("ran")
test.addWord("rune")
test.addWord("runner")
test.addWord("runs")
test.addWord("add")
test.addWord("adds")
test.addWord("adder")
test.addWord("addee")

r = test.search("ran")
print(r)
r = test.search("ru.n.e")
print(r)
r = test.search("add")
print(r)
r = test.search("add.")
print(r)
r = test.search("adde.")
print(r)
r = test.search(".an.")
print(r)
r = test.search("...s")
print(r)
r = test.search("....e.")
print(r)
r = test.search(".......")
print(r)
r = test.search("..n.r")
print(r)
r = test.search("..n..r")
print(r)

