# ### WORD SEARCH II

# Given an m x n board of characters and a list of strings words, return all words on the board.

# Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

# https://leetcode.com/problems/word-search-ii/description/

class TrieNode:
    def __init__(self):
        self.children = {} #can also do array
        self.end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root

        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            
            curr = curr.children[char]
        
        curr.end_of_word = True
    
    def search(self, word:str) -> bool:
        curr = self.root

        for char in word:
            if char not in curr.children:
                return False
            
            curr = curr.children[char]
        
        return curr.end_of_word

    def starts_with(self, prefix: str) -> bool:
        curr = self.root

        for char in prefix:
            if char not in curr.children:
                return False
            
            curr = curr.children[char]
        
        return True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # for each word, do dfs on board ?

        # if make a trie, can potentially reduce tc

        trie = Trie()

        for word in words:
            trie.insert(word)
        
        ans = set()
        # every word has its own seen
        seen = set()

        def dfs(i, j, node, word):
            seen.add((i, j)) 

            if node.end_of_word == True:
                ans.add(''.join(word))

            dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]

            for dx, dy in dirs:
                x, y = i + dx, j + dy

                if x < 0 or y < 0 or x == len(board) or y == len(board[0]) or (x, y) in seen:
                    continue

                if node.children and board[x][y] in node.children:
                    word.append(board[x][y])
                    dfs(x, y, node.children[board[x][y]], word)
                    word.pop()
            
            seen.remove((i, j))

        starts = trie.root.children

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] in starts:
                    node = trie.root.children[board[i][j]]
                    dfs(i, j, node, [board[i][j]])

        return list(ans)
        