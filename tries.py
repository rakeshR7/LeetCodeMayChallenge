"""
Implement a trie with insert, search, and startsWith methods.

Example:

Trie trie = new Trie();

trie.insert("apple");
trie.search("apple");   // returns true
trie.search("app");     // returns false
trie.startsWith("app"); // returns true
trie.insert("app");   
trie.search("app");     // returns true

"""

class TreeNode:
    
    def __init__(self,value):
        self.val = value
        self.children = {}
        self.end = False

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TreeNode(None)
        

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        parent = self.root
        for i, char in enumerate(word):
            if char not in parent.children:
                parent.children[char] = TreeNode(char)
            parent = parent.children[char]
            if(i == len(word)-1):
                parent.end = True
            
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        parent = self.root
        for i in word:
            if i not in parent.children:
                return False
            parent = parent.children[i]
        return parent.end
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        parent = self.root
        for i in prefix:
            if i not in parent.children:
                return False
            parent = parent.children[i]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
