class LinkedNode:
    def __init__(self):
        self.children = {}
        self.word = False

class WordDictionary:

    def __init__(self):
        self.root = LinkedNode()

    def addWord(self, word: str) -> None:
        addNode = self.root
        for c in word:
            if c not in addNode.children:
                addNode.children[c] = LinkedNode()
            addNode = addNode.children[c]
        addNode.word = True
        

    def search(self, word: str) -> bool:
        def dfs(j, root):
            cur = root

            for i in range(j, len(word)):
                c = word[i]
                if c == ".":
                    for child in cur.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False
                else:
                    if c not in cur.children:
                        return False
                    cur = cur.children[c]
            return cur.word

        return dfs(0, self.root)

        
