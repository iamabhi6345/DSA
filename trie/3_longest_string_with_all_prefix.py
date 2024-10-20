                            
class Node:
    # Array to store links to child nodes,
    # each index represents a letter
    def __init__(self):
        self.links = [None] * 26
        # Flag indicating if the node
        # marks the end of a word
        self.flag = False

    # Check if the node contains
    # a specific key (letter)
    def containsKey(self, ch):
        return self.links[ord(ch) - ord('a')] is not None

    # Insert a new node with a specific
    # key (letter) into the Trie
    def put(self, ch, node):
        self.links[ord(ch) - ord('a')] = node

    # Get the node with a specific
    # key (letter) from the Trie
    def get(self, ch):
        return self.links[ord(ch) - ord('a')]

    # Set the current node
    # as the end of a word
    def setEnd(self):
        self.flag = True

    # Check if the current node
    # marks the end of a word
    def isEnd(self):
        return self.flag


class Trie:
    # Constructor to initialize the
    # Trie with an empty root node
    def __init__(self):
        self.root = Node()

    # Inserts a word into the Trie
    # Time Complexity O(len), where len
    # is the length of the word
    def insert(self, word):
        node = self.root
        for ch in word:
            if not node.containsKey(ch):
                # Create a new node for
                # the letter if not present
                node.put(ch, Node())
            # Move to the next node
            node = node.get(ch)
        # Mark the end of the word
        node.setEnd()

    # Method to check if a given string is
    # a prefix of any word in the Trie
    def checkIfPrefixExists(self, word):
        node = self.root
        for ch in word:
            if node.containsKey(ch):
                # Move to the child node corresponding
                # to the current character
                node = node.get(ch)
                if not node.isEnd():
                    # If the current node does not mark
                    # the end of a word, return false
                    return False
            else:
                # If the current character does not
                # exist as a child node, return false
                return False
        # If all characters are found and
        # marked as the end of a word, return true
        return True


# Function to find the longest complete string
# in the given array of strings
def completeString(n, a):
    trie = Trie()
    # Insert each string from the
    # array into the Trie
    for word in a:
        trie.insert(word)
    longest = ""
    # Iterate through each
    # string in the array
    for word in a:
        # Check if the current string is a
        # prefix of any word in the Trie
        if trie.checkIfPrefixExists(word):
            # If it is a prefix, compare its length
            # with the current longest complete string
            if len(word) > len(longest):
                longest = word
            elif len(word) == len(longest) and word < longest:
                # If lengths are equal, choose the
                # lexicographically smaller one
                longest = word
    # If no complete string
    # is found, return "None"
    if longest == "":
        return "None"
    return longest


strings = ["striver", "strive", "striving", "striven", "strived", "striv"]
longestComplete = completeString(len(strings), strings)
print("Longest complete string:", longestComplete)
                           
                        