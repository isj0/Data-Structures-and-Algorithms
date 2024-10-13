import trie_node


class Trie:
    
    def __init__(self):
      self.root = trie_node.TrieNode()
    def search(self, word):
        current_node = self.root

        for char in word:
            if current_node.children.get(char):
                current_node = current_node.children[char]
            else:
                return None

        return current_node
    def insert(self, word):
        current_node = self.root

        for char in word:
            if current_node.children.get(char):
                current_node = current_node.children[char]
            else:
                new_node = trie_node.TrieNode()
                current_node.children[char] = new_node
                current_node = new_node

        current_node.children["*"] = None
    def collect_all_words(self, words, node=None, word=""):
        current_node = node or self.root
        for key, child_node in current_node.children.items():
            if key == "*":
                words.append(word)
            else:
                self.collect_all_words(words, child_node, word + key)

        return words
    def autocomplete(self, prefix):
        current_node = self.search(prefix)

        if not current_node:
            return None
        
        return self.collect_all_words([], current_node)
    def traverse(self, node=None):
        current_node = node or self.root

        for key, child_node in current_node.children.items():
            print(key)

            if key != "*":
                self.traverse(child_node)
    def autocorrect(self, word):
        current_node = self.root
        word_found_so_far = ""

        for char in word:
            if current_node.children.get(char): 
                word_found_so_far += char 
                current_node = current_node.children.get(char)
            else:
                return word_found_so_far + \
                    self.collect_all_words([], current_node)[0]

        return word
