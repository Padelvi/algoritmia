class TrieNode:
    def __init__(self, char: str|None = None):
        self.children = dict()
        self.is_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for ch in word:
            node = node.children.setdefault(ch, TrieNode())
        node.is_word = True

    def search_word(self, word):
        node = self._walk(word)
        return node is not None and node.is_word

    def search_prefix(self, prefix):
        return self._walk(prefix) is not None

    def _walk(self, s):
        node = self.root
        for ch in s:
            if ch not in node.children:
                return None
            node = node.children[ch]
        return node


trie = Trie()
for word in ["car", "card", "care", "dog"]:
    trie.insert(word)

print("search(card):     ", trie.search("card"))
print("search(ca):       ", trie.search("ca"))
print("starts_with(ca):  ", trie.starts_with("ca"))
print("starts_with(do):  ", trie.starts_with("do"))
print("starts_with(cat): ", trie.starts_with("cat"))