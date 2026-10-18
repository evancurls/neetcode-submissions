class TrieNode:
    def __init__(self, val):
        self.val: str = val
        self.isTerminal = False
        self.nextLetters = {}

class PrefixTree:
    def __init__(self):
        self.root = TrieNode(val="BASE ROOT")

    def insert(self, word: str) -> None:
        base = self.root
        for c in word:
            if c not in base.nextLetters:
                temp = TrieNode(c)
                base.nextLetters[c] = temp
            base = base.nextLetters[c]
        base.isTerminal = True


    def search(self, word: str) -> bool:
        base = self.root
        for c in word:
            if c not in base.nextLetters:
                return False
            base = base.nextLetters[c]
        if base.isTerminal:
            return True
        else:
            return False

    def startsWith(self, prefix: str) -> bool:
        base = self.root
        for c in prefix:
            if c not in base.nextLetters:
                # print(f"{c} not in {base.val}'s nextLetters; returning False")
                return False
            base = base.nextLetters[c]
        return True