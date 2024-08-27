"""   
Problem statement
You are given an array 'prices' of size 'n', denoting the price of stocks on 'n' days.



Rahul can buy one stock at a time, and he must sell it before buying stock on another day.



The entire transaction of selling and buying the stock requires some transaction fee, given as 'fee'.



Find the maximum profit Rahul can achieve by trading on the stocks.



Example :
Input: 'prices' =  [1, 2, 3] and 'fee' = 1

Output: 1

Explanation: We can generate the maximum profit of 1 by buying the stock on the first day for price = 1 and then selling it on the third day for price = 3.

The profit will be: 3 - 1 - 1(transaction fee) = 1
Detailed explanation ( Input/output format, Notes, Images )
Sample Input 1 :
3 1
1 2 3


Sample Output 1 :
1


Explanation Of Sample Input 1 :
We can generate the maximum profit of 1 by buying the stock on the first day for price = 1 and then selling it on the third day for price = 3.                                                                                                     
The profit will be: 3 - 1 - 1(transaction fee) = 1


Sample Input 2 :
4 2
1 3 5 6


Sample Output 2 :
3


Expected time complexity :
The expected time complexity is O(n).


Constraints :
1 <= 'n' <= 10 ^ 4
0 <= 'prices[i]' <= 10 ^ 5
0 <= 'fee'<= 10 ^ 5

"""

from typing import List

def solve(ind , buy , values , n , dp,fee):
    if ind>=n:
        return 0
    
    if dp[ind][buy]!=-1:
        return dp[ind][buy]
    
    if buy==True:
        profit = max ( -values[ind] + solve(ind+1 , False , values , n , dp,fee),
                     0 + solve(ind+1 , buy , values , n,dp,fee))
    else:
        profit = max (values[ind]-fee + solve(ind+1 , True , values , n,dp,fee),
                    0+solve(ind+1 , buy , values , n,dp,fee))
    
    dp[ind][buy] = profit
    return dp[ind][buy]



def maximumProfit(prices: List[int], n: int, fee: int) -> int:
    # write your code here
    n= len(prices)
    dp= [[-1]*2 for _ in range(n)]
    return solve(0,True,prices,n,dp,fee)




from typing import List

def maximumProfit(prices: List[int], n: int, fee: int) -> int:
    # write your code here
    n = len(prices)
    dp= [[0]*2 for _ in range(n+1)]

    for ind in range(n-1,-1,-1):
        for buy in range(2):
            if buy:
                dp[ind][buy]=max(-prices[ind]+dp[ind+1][0] ,dp[ind+1][1])
            else:
                dp[ind][buy] = max(prices[ind]-fee + dp[ind+1][1] , dp[ind+1][0])


    return dp[0][1]