class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False
    def addword(self, word):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.word = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for w in words:
            root.addword(w)
        res, valid = set(), set()
        rows, cols = len(board), len(board[0])
        def dfs(r, c, node, word):
            if (r<0 or c <0 or r >=rows or c >=cols or
                (r, c) in valid or
                board[r][c] not in node.children):
                return
            valid.add((r, c))
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.word:
                res.add(word)
            dfs(r+1, c, node, word)
            dfs(r-1, c, node, word)
            dfs(r, c+1, node, word)
            dfs(r, c-1, node, word)
            valid.remove((r, c))
        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root, "")
        return list(res)