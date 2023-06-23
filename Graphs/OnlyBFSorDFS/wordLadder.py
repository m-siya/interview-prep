# ### WORD LADDER

# A transformation sequence from word beginWord to word endWord using a dictionary wordList is a 
# sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

# Every adjacent pair of words differs by a single letter.
# Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
# sk == endWord
# Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the 
# shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists.

# https://leetcode.com/problems/word-ladder/description/

# method -> all words that differ by 1 letter are connected nodes in a graph. 
# build an adjacency list of form {pattern: [word+]}
# eg. patterns of hot -> ?ot, h?t, ho?
# then simple bfs to find the shortest path
# the bfs needs a for loop nested inside the while loop to sort of get the snapshot?

# time complexity -> O(n * m * m) to build the adj list + O(n * n * m) for bfs

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList: return 0
        #construct adj list
        adj_list = {}

        wordList.append(beginWord)
        for word in wordList:
            #eg - hot -> ?ot, h?t, ho?
            for i in range(len(word)):
                pattern = word[:i] + "?" + word[i + 1:]
                if pattern in adj_list:
                    adj_list[pattern].append(word)
                else:
                    adj_list[pattern] = [word]

      
        #print(adj_list)

        #bfs to find shortest path
        path = 1
        visited = set()
        q = deque()
        q.append(beginWord)
        visited.add(beginWord)

        while q:
            #print(q)
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord: return path
                #visited.add(word)

                for j in range(len(word)):
                    pattern = word[:j] + "?" + word[j + 1:]
                    neighbours = adj_list[pattern]

                    for neighbour in neighbours:
                        if neighbour not in visited:
                            visited.add(neighbour)
                            q.append(neighbour)
            path += 1

        return 0
