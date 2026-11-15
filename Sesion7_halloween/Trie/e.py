class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for ch in word:
            node = node.children.setdefault(ch, TrieNode())
        node.is_word = True

    def search(self, word):
        node = self._walk(word)
        return node is not None and node.is_word

    def starts_with(self, prefix):
        return self._walk(prefix) is not None

    def _walk(self, s):
        node = self.root
        for ch in s:
            if ch not in node.children:
                return None
            node = node.children[ch]
        return node


trie = Trie()
n = int(input())

runas = []
for _ in range(n):
    runas.append(input())
for word in runas:
    trie.insert(word)

for runa in runas:
    for i in range(1,len(runa)):
        if not trie.search(runa[:i]):
            print(i)
            break
    else:
        print(len(runa))