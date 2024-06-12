# Trie : Implementations, Insert & Search 
class TrieNode:
     
    # Trie node class
    def __init__(self):
        self.children = [None for _ in range(26)]
 
        # isEndOfWord is True if node represent the end of the word
        self.isEndOfWord = False
        

class Trie:
     
    # Trie data structure class
    def __init__(self):
        self.root = self.getNode()
 
    def getNode(self):
     
        # Returns new trie node (initialized to NULLs)
        return TrieNode()
 
    def _charToIndex(self,ch):
         
        # private helper function
        # Converts key current character into index
        # use only 'a' through 'z' and lower case
         
        return ord(ch)-ord('a')
 
 
    def insert(self,word):
         
        # If not present, inserts key into trie
        # If the key is prefix of trie node,
        # just marks leaf node
        curr = self.root
        length = len(word)
        for level in range(length):
            index = self._charToIndex(word[level])
 
            # if current character is not present
            if curr.children[index] is None:
                curr.children[index] = self.getNode()
            curr = curr.children[index]
 
        # mark last node as leaf
        curr.isEndOfWord = True
 
    def search(self, word):
         
        # Search word in the trie
        # Returns true if word presents
        # in trie, else false
        curr = self.root
        length = len(word)
        for level in range(length):
            index = self._charToIndex(word[level])
            if curr.children[index] is None:
                return False
            curr = curr.children[index]
 
        return curr.isEndOfWord
 


    
 # Trie object
t = Trie()
 
# Construct trie
for word in ["the","by","their"]:
    t.insert(word)

# Search for different keys
print(t.search("by"))