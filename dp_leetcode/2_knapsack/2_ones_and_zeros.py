"""  
474. Ones and Zeroes
Solved
Medium
Topics
Companies
You are given an array of binary strings strs and two integers m and n.

Return the size of the largest subset of strs such that there are at most m 0's and n 1's in the subset.

A set x is a subset of a set y if all elements of x are also elements of y.

 

Example 1:

Input: strs = ["10","0001","111001","1","0"], m = 5, n = 3
Output: 4
Explanation: The largest subset with at most 5 0's and 3 1's is {"10", "0001", "1", "0"}, so the answer is 4.
Other valid but smaller subsets include {"0001", "1"} and {"10", "1", "0"}.
{"111001"} is an invalid subset because it contains 4 1's, greater than the maximum of 3.
Example 2:

Input: strs = ["10","0","1"], m = 1, n = 1
Output: 2
Explanation: The largest subset is {"0", "1"}, so the answer is 2.
 

Constraints:

1 <= strs.length <= 600
1 <= strs[i].length <= 100
strs[i] consists only of digits '0' and '1'.
1 <= m, n <= 100

"""
class Solution:
    def solve(self , i ,strs,  m , n ,dp):
        if i<0:
            return 0
        if m<=0 and  n<=0:
            return 0
        
        if dp[i][m][n]!=-1:
            return dp[i][m][n]
        
        c0=strs[i].count('0')
        c1=strs[i].count('1')

        nottake = self.solve(i-1 , strs , m , n , dp)
        take =0

        if c0 <= m and c1 <=n:
            take = 1 + self.solve(i-1 , strs , m-c0 , n-c1 , dp)
        
        dp[i][m][n] = max(take , nottake)
        return dp[i][m][n]


    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        l= len(strs)
        dp= [[ [-1]*(n+1)  for _ in range(m+1)] for _ in range(l)]
        return self.solve(len(strs)-1 , strs , m , n , dp)
        























# ???????????????????????????
class Solution:
    def solve(self , i ,strs,  m , n ,dp):
        if i<0:
            return 0
        if m<=0 and  n<=0:
            return 0
        
        if (i,m,n) in dp:
            return dp[(i,m,n)]
        c0=strs[i].count('0')
        c1=strs[i].count('1')

        nottake = self.solve(i-1 , strs , m , n , dp)
        take =0

        if c0 <= m and c1 <=n:
            take = 1 + self.solve(i-1 , strs , m-c0 , n-c1 , dp)
        
        dp[(i,m,n)] = max(take , nottake)
        return dp[(i,m,n)]


    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        l= len(strs)
        # dp= [[ [-1]*(n+1)  for _ in range(m+1)] for _ in range(l)]
        dp={}
        return self.solve(len(strs)-1 , strs , m , n , dp)
        