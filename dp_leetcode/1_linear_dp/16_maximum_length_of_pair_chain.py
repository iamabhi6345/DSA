"""  
You are given an array of n pairs pairs where pairs[i] = [lefti, righti] and lefti < righti.

A pair p2 = [c, d] follows a pair p1 = [a, b] if b < c. A chain of pairs can be formed in this fashion.

Return the length longest chain which can be formed.

You do not need to use up all the given intervals. You can select pairs in any order.

 

Example 1:

Input: pairs = [[1,2],[2,3],[3,4]]
Output: 2
Explanation: The longest chain is [1,2] -> [3,4].
Example 2:

Input: pairs = [[1,2],[7,8],[4,5]]
Output: 3
Explanation: The longest chain is [1,2] -> [4,5] -> [7,8].
 

Constraints:

n == pairs.length
1 <= n <= 1000
-1000 <= lefti < righti <= 1000

"""


# LIS approach  
# we are sorting because in question it is given we can choose in any order
# so after sorting its become LIS


# tabulation

class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        n= len(pairs)
        dp = [1]*n
        # pairs.sort()
        pairs.sort(key = lambda x:x[1])
        # sorting based on second index make it faster
        ans =1

        for i in range(n):
            for j in range(i):
                if pairs[i][0] > pairs[j][1]  and 1 + dp[j] > dp[i]:
                    dp[i]=1+dp[j]
            ans = max (ans , dp[i])
        return ans



# memoization
class Solution:
    def solve(self,ind,prev,dp , pairs):
        if ind==len(pairs):
            return 0
        
        if dp[ind][prev+1]!=-1:
            return dp[ind][prev+1]
        
        take = 0
        if prev==-1 or pairs[ind][0]>pairs[prev][1]:
            take = 1 + self.solve(ind+1, ind , dp , pairs)
        nottake = self.solve(ind+1 , prev ,dp,pairs)

        dp[ind][prev+1]=max(take , nottake)
        return dp[ind][prev+1]



    def findLongestChain(self, pairs: List[List[int]]) -> int:
        # pairs.sort()
        pairs.sort(key = lambda x:x[1])
        # sorting by second index mkae it faster
        n= len(pairs)
        dp=[ [-1]*(n+1) for _ in range(n)]
        return self.solve(0,-1,dp,pairs)
