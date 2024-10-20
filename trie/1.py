class node:
    def __init__(self ):
        self.links = [None]*26
        self.flag = False
        
    
    def containskey(self , key):
        return self.links[ord(key) - ord('a')] is not None 
    
    def put(self , ch , new_node):
        self.links[ord(ch) - ord('a')] = new_node 
        
    def get(self , ch):
        return self.links[ord(ch) - ord('a')]

    def setEnd(self):
        self.flag = True   
    
    def isEnd(self):
        return self.flag 





class Trie:
    def __init__(self):
        self.root = node()
    
    def insert(self, word):
        nd = self.root
        for ch in word:
            if not nd.containskey(ch):
                nd.put(ch , node())
            
            nd = nd.get(ch)
        nd.setEnd()
    
    def search(self , word):
        nd = self.root
        for ch in word:
            if not nd.containskey(ch):
                return False
            nd = nd.get(ch)
        return nd.isEnd()


    def startsWith(self, prefix):
        nd = self.root 
        for ch in prefix:
            if not nd.containskey(ch):
                return False
            nd = nd.get(ch)
        return True






if __name__ == "__main__":
    trie = Trie()
    print("Inserting words: Striver, Striving, String, Strike")
    trie.insert("striver")
    trie.insert("striving")
    trie.insert("string")
    trie.insert("strike")

    print("Search if Strawberry exists in trie: " +
          ("True" if trie.search("strawberry") else "False"))

    print("Search if Strike exists in trie: " +
          ("True" if trie.search("strike") else "False"))

    print("If words in Trie start with Stri: " +
          ("True" if trie.startsWith("stri") else "False"))





