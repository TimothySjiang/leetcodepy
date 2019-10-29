class TrieNode():
    def __init__(self, val):
        self.val = val
        self.child = {}
        self.isword = False


class WordDictionary:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode(None)

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        node = self.root
        for ch in word:
            if ch not in node.child:
                node.child[ch] = TrieNode(ch)
            node = node.child[ch]
        node.isword = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        node = self.root
        stack = [(node, 0)]
        while stack:
            node, i = stack.pop()
            if i == len(word):
                if node.isword:
                    return True
                else:
                    continue
            ch = word[i]
            if ch != '.':
                if ch in node.child:
                    stack.append((node.child[ch], i + 1))
            else:
                for c in ['a', 'b', 'c', 'd', 'e', 'f', 'g',
                          'h', 'i', 'j', 'k', 'l', 'm', 'n',
                          'o', 'p', 'q', 'r', 's', 't', 'u',
                          'v', 'w', 'x', 'y', 'z']:
                    if c in node.child:
                        stack.append((node.child[c], i + 1))
        return False


