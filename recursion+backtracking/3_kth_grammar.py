"""
    We build a table of n rows (1-indexed). We start by writing 0 in the 1st row. Now in every subsequent row,
    we look at the previous row and replace each occurrence of 0 with 01, and each occurrence of 1 with 10.

    For example, for n = 3, the 1st row is 0, the 2nd row is 01, and the 3rd row is 0110.

    Given two integer n and k, return the kth (1-indexed) symbol in the nth row of a table of n rows.

    

    Example 1:

    Input: n = 1, k = 1
    Output: 0
    Explanation: row 1: 0
    
    
    0
    01
    0110
    01101001
    
    
    observations
            first half are exactly match of above 
            second half are not of above

"""

# ---------------------------brute force -----------------------------
def kthGrammar1( n: int, k: int) -> int:
    
    def rep(s: str) -> str:
        replacement = {'0': '01', '1': '10'}
        result = ''.join([replacement[char] for char in s])
        return result

    s="0"
    for i in range(1,n,1):
        s=rep(s)
    return int(s[k-1])


"""
it can give memory limits exceeded becaure are storing 2^(n-1)
if n is larger in range 4k it will throw error
we just have to return a single integer value so follow observation
"""
# -------------------------------------------------------------------------------



"""
    time complexity = O(n)
    space complexity = O(n)
"""


class Solution:
    def kthGrammar(self, n: int, k: int) -> int:

        if n==1:
            return 0
        
        midpoint= 2**(n-2)

        if k <= midpoint :
            return self.kthGrammar(n-1,k)
        else :
            return  (1 - self.kthGrammar(n-1 , k-midpoint))

