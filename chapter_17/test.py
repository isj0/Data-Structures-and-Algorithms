import trie


def assert_equal(x, y):
    if x == y:
        print(".")
    else:
        print("FAIL")


# Insert and Search
print("Insert and Search")
t = trie.Trie()
t.insert("cat")
t.insert("dog")
t.insert("catnip")
t.insert("catnap")
t.insert("category")
assert_equal(t.search("catnap").children, {'*': None})
assert_equal(t.search("catnax"), None)

# Collect all words
print("Collect all words")
words = t.collect_all_words([])
assert_equal('cat' in words, True)
assert_equal('dog' in words, True)
assert_equal('catnip' in words, True)
assert_equal('catnap' in words, True)
assert_equal('category' in words, True)

# Autocomplete
print("Autocomplete")
suggestions = t.autocomplete('ca')
assert_equal('t' in suggestions, True)
assert_equal('tnip' in suggestions, True)
assert_equal('tnap' in suggestions, True)
assert_equal('tegory' in suggestions, True)
assert_equal('dog' in suggestions, False)

# Autocorrect
print("Autocorrect")
assert_equal(t.autocorrect('catnar'), 'catnap')
assert_equal(t.autocorrect('caxasfdij'), 'cat')

# Traverse
print("Traverse")
t.traverse()
