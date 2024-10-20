"""

Problem statement
Given a string 'S', you are supposed to return the number of distinct substrings(including empty substring) of the given string. You should implement the program using a trie.

Note :
A string ‘B’ is a substring of a string ‘A’ if ‘B’ that can be obtained by deletion of, several characters(possibly none) from the start of ‘A’ and several characters(possibly none) from the end of ‘A’. 

Two strings ‘X’ and ‘Y’ are considered different if there is at least one index ‘i’  such that the character of ‘X’ at index ‘i’ is different from the character of ‘Y’ at index ‘i’(X[i]!=Y[i]).
Detailed explanation ( Input/output format, Notes, Images )
Constraints :
1 <= T <= 5
1 <= |S| <= 10^3

‘S’ contains only lowercase English letters.

Time Limit: 1 sec
Sample Input 1 :
2
sds
abc
Sample Output 1 :
6
7
Explanation of Sample Input 1 :
In the first test case, the 6 distinct substrings are { ‘s’,’ d’, ”sd”, ”ds”, ”sds”, “” }

In the second test case, the 7 distinct substrings are {‘a’, ‘b’, ‘c’, “ab”, “bc”, “abc”, “” }.
Sample Input 2 :
2
aa
abab
Sample Output 2 :
3
8
Explanation of Sample Input 2 :
In the first test case, the two distinct substrings are {‘a’, “aa”, “” }.

In the second test case, the seven distinct substrings are {‘a’, ‘b’, “ab”, “ba”, “aba”, “bab”, “abab”, “” }


Hints:
1. Can you think about a data structure that can be used to store the distinct substrings?
2. Can you think about using the fact that every substring of ‘S’ is a prefix of some suffix string of ‘S’?
3. Try to insert every suffix of the string in Trie.    


"""


# def countDistinctSubstrings(s):
#     st= set()
#     st.add("")
#     for i in range(len(s)):
#         for j in range(len(s)-i):
#             st.add(s[i:i+j+1])
#     return len(st)




                                
                     
class Node:
    """
    Node structure representing
    each node in the trie
    """

    def __init__(self):
        self.links = [None] * 26  
        # Array of pointers to child nodes,
        # each corresponding to a letter
        # of the alphabet
        self.flag = False  
        # Flag indicating if the current
        # node represents the end of a substring

    def containsKey(self, ch):
        """
        Method to check if a specific character key
        exists in the children of the current node
        """
        # Check if the current node has a child node
        # corresponding to character 'ch'
        return self.links[ord(ch) - ord('a')] is not None

    def get(self, ch):
        """
        Method to get the child node corresponding
        to a specific character key
        """
        # Get the child node
        # corresponding to character 'ch'
        return self.links[ord(ch) - ord('a')]

    def put(self, ch, node):
        """
        Method to insert a new child
        node with a specific character key
        """
        # Insert a new child
        # node for character 'ch'
        self.links[ord(ch) - ord('a')] = node

    def setEnd(self):
        """
        Method to mark the current
        node as the end of a substring
        """
        # Mark the current node
        # as the end of a substring
        self.flag = True

    def isEnd(self):
        """
        Method to check if the current
        node marks the end of a substring
        """
        # Check if the current node
        # marks the end of a substring
        return self.flag


def countDistinctSubstrings(s):
    """
    Function to count the number of
    distinct substrings in the given string
    """
    root = Node()  
    # Creating the root
    # node of the trie
    cnt = 0  
    # Counter to keep track
    # of distinct substrings
    n = len(s)  
    # Length of the input string

    # Nested loops to iterate through all
    # possible substrings of the input string
    for i in range(n):  
        # Iterate through each
        # starting position of the substring
        node = root  
        # Start from the root for each substring
        for j in range(i, n):  
            # Iterate through each character of the substring
            # If the current character is not a child
            # of the current node, insert it as a new child node
            if not node.containsKey(s[j]):
                node.put(s[j], Node())  
                # Insert a new child
                # node for character s[j]
                cnt += 1  
                # Increment the counter
                # since a new substring is found
            node = node.get(s[j])  
            # Move to the child node
            # corresponding to character s[j]

    return cnt + 1  
    # Return the total count of distinct substrings
    # (+1 to account for the input string itself)


if __name__ == "__main__":
    s = "striver"  
    # Input string
    print("Current String:", s)
    print("Number of distinct substrings:", countDistinctSubstrings(s))  

