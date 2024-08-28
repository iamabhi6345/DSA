"""  
Given a string s, partition s such that every 
substring
 of the partition is a 
palindrome
.

Return the minimum cuts needed for a palindrome partitioning of s.

 

Example 1:

Input: s = "aab"
Output: 1
Explanation: The palindrome partitioning ["aa","b"] could be produced using 1 cut.
Example 2:

Input: s = "a"
Output: 0
Example 3:

Input: s = "ab"
Output: 1
 

Constraints:

1 <= s.length <= 2000
s consists of lowercase English letters only.

"""


class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        dp = [0]*(n+1)

        for i in range(n-1,-1,-1):
            mini = int(1e8)
            for j in range(i , n):
                if s[i:j + 1] == s[i:j + 1][::-1]:
                    cost = 1 + dp[j+1]
                    mini = min(mini , cost)
            dp[i]=mini

        return dp[0]-1

"""  
is palindrome function can cause Time limit Exceeded so use
s[i:j + 1] == s[i:j + 1][::-1]:
above will prevent from TLE
"""

class Solution:
    
    def solve(self, ind , dp , s ):
        if ind==len(s):
            return 0
        if dp[ind]!=-1:
            return dp[ind]
        
        mini = int(1e8)
        for j in range(ind , len(s) , 1):
            if s[ind:j + 1] == s[ind:j + 1][::-1]:
                cost = 1 + self.solve(j+1,dp,s)
                mini = min(cost  , mini)
        
        dp[ind] = mini
        return dp[ind]



    def minCut(self, s: str) -> int:
        dp = [-1]*len(s)
        return self.solve(0,dp,s)-1

""" 
???????????? above will not give TLE but below will give TLE
"""

class Solution:
    def __is_palindrome(self , i , j , s):
        while(i<j):
            if s[i]!=s[j]:
                return False
            i+=1
            j-=1
        return True

    def solve(self, ind , dp , s ):
        if ind==len(s):
            return 0
        if dp[ind]!=-1:
            return dp[ind]

        mini = int(1e8)
        for j in range(ind , len(s) , 1):
            if self.__is_palindrome(ind , j, s):
                cost = 1 + self.solve(j+1,dp,s)
                mini = min(cost  , mini)
        dp[ind] = mini
        return dp[ind]



    def minCut(self, s: str) -> int:
        dp = [-1]*len(s)
        return self.solve(0,dp,s)-1
