

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
