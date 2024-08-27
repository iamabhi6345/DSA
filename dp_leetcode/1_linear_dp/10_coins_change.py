""" 
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

 

Example 1:

Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
Example 3:

Input: coins = [1], amount = 0
Output: 0
 

Constraints:

1 <= coins.length <= 12
1 <= coins[i] <= 231 - 1
0 <= amount <= 104

"""

class Solution:
    def f(self , ind , tar , coins , dp):

        

        if tar==0:
            return 0

        if ind==0:
            if tar%coins[ind]==0:
                return tar//coins[0]
            else:
                return int(1e9)

        if dp[ind][tar]!=-1:
            return dp[ind][tar]
        
        take =int(1e9)
        if tar>=coins[ind]:
                 take = 1 + self.f(ind , tar-coins[ind] , coins,dp)

        nottake= self.f(ind-1, tar , coins,dp)
        dp[ind][tar] =  min(take , nottake)
        return dp[ind][tar]

    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        dp = [[-1]*(amount+1) for _ in range(n)]
        ans = self.f(n-1,amount,coins , dp)
        if ans>=int(1e9):
            return -1
        return ans
