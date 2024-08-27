""" 
Given an integer n, return the number of structurally unique BST's (binary search trees) which has exactly n nodes of unique values from 1 to n.

 

Example 1:


Input: n = 3
Output: 5
Example 2:

Input: n = 1
Output: 1
"""

class Solution:
    def numTrees(self, n: int) -> int:
        ans = [0]*(n+1)
        ans[0]=1
        ans[1]=1

        for i in range(2,n+1):
            for j in range(1, i+1):
                ans[i]+= ans[j-1]*ans[i-j]

        return ans[n]
