"""  
650. 2 Keys Keyboard
Solved
Medium
Topics
Companies
Hint
There is only one character 'A' on the screen of a notepad. You can perform one of two operations on this notepad for each step:

Copy All: You can copy all the characters present on the screen (a partial copy is not allowed).
Paste: You can paste the characters which are copied last time.
Given an integer n, return the minimum number of operations to get the character 'A' exactly n times on the screen.

 

Example 1:

Input: n = 3
Output: 3
Explanation: Initially, we have one character 'A'.
In step 1, we use Copy All operation.
In step 2, we use Paste operation to get 'AA'.
In step 3, we use Paste operation to get 'AAA'.
Example 2:

Input: n = 1
Output: 0


"""


class Solution:
    def minSteps(self, n: int) -> int:
        dp={}
        def solve(counts , paste):
            if counts == n:
                return 0
            if counts >n:
                return 1e9
            
            if (counts , paste) in dp:
                return dp[(counts, paste)]
            
            paste_only = 1 + solve(counts + paste , paste)

            copy_paste = 2 + solve(counts + counts , counts)

            dp[(counts , paste)]  = min(paste_only , copy_paste)
            return dp[(counts , paste)]
        
        if n==1:
            return 0
        return 1+ solve(1 , 1)
""" 
above t.c = O(n**2)  , s.c =O(n**2)

below t.c =O(n)      , s.c =O(1)

logic  for ----->  if n % paste ==0: 
to divide into fix interval  , 
if n=8 if n=4 then in next 2 (1 copy + 1 paste) operation we reach there
so internal gives us optimization

"""


class Solution:
    def minSteps(self, n: int) -> int:
        copy =0 
        paste =1
        operation =0 

        while paste !=n:
            if n % paste ==0:
                copy=paste
                operation+=1
            
            paste+=copy
            operation+=1
        
        return operation

