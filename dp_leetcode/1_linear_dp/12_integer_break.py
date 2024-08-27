"""   
Given an integer n, break it into the sum of k positive integers, where k >= 2, and maximize the product of those integers.

Return the maximum product you can get.

 

Example 1:

Input: n = 2
Output: 1
Explanation: 2 = 1 + 1, 1 × 1 = 1.
Example 2:

Input: n = 10
Output: 36
Explanation: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36.
 

Constraints:

2 <= n <= 58

"""

class Solution:
    def solve(self,n , dp):
        if n==1:
            return 1
        if dp[n]!=-1:
            return dp[n]
        
        ans = n-1
        for i in range(1 , n//2+1):
            tmp = i* max ( n-i, self.solve(n-i,dp))
            ans=max(tmp , ans)
        dp[n]=ans
        return dp[n]
        

    def integerBreak(self, n: int) -> int:
        dp=[-1]*(n+1)
        return self.solve(n,dp)
