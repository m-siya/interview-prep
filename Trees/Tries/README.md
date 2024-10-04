## Trie

### Resources
- https://www.youtube.com/watch?v=oobqoCJlHA0
- https://www.youtube.com/watch?v=dBGUmUQhjaM&list=PLgUwDviBIf0pcIDCZnxhv0LkHf5KzG9zp

- A tree DS used for storing collections of strings. 
- if 2 strings have a common prefix, they will have a common parent
- good of storing dictionaries, spellchecker, autocomplete
- can sort strings lexicographically in tries
- take less space than a hash table

### ADT Functions
1. insert(word) - to insert a string'word' in trie
2. search(word) - to check if a string 'word' is present in trie or not
3. starts_with(prefix) - to checl if there is any string in trie which starts with prefix 'prefix'


```Python
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

```