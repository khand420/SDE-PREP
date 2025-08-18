# ✅ What is a Trie?
# A Trie is a special kind of tree used to efficiently store and retrieve strings, especially useful for:

# Autocomplete

# Spell checking

# Prefix searches

# Each node represents a character, and a path from root to a node spells out a word or prefix.

# 🔧 Operations We’ll Implement
# insert(word) – Add a word to the trie

# search(word) – Check if a word exists in the trie

# startsWith(prefix) – Check if any word starts with the given prefix




class TrieNode:
    def __init__(self):
        self.children = {}  # key: character, value: TrieNode
        self.is_end_of_word = False  # marks end of word

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_end_of_word = True

    def search(self, word):
        node = self._search_prefix(word)
        return node is not None and node.is_end_of_word

    def startsWith(self, prefix):
        return self._search_prefix(prefix) is not None

    def _search_prefix(self, prefix):
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return None
            node = node.children[ch]
        return node


trie = Trie()
trie.insert("apple")
trie.insert("app")

print(trie.search("apple"))     # True
print(trie.search("app"))       # True
print(trie.search("appl"))      # False
print(trie.startsWith("app"))   # True
print(trie.startsWith("apz"))   # False
