"""   
Problem statement
You are given a list of stock prices of size 'n' called ‘prices’, where ‘prices[i]’ represents the price on ‘i’th day.



Your task is to calculate the maximum profit you can earn by trading stocks if you can only hold one stock at a time.



After you sell your stock on the ‘i’th day, you can only buy another stock on ‘i + 2’ th day or later.



Example:
Input: 'prices' = [4, 9, 0, 4, 10]

Output: 11

Explanation:
You are given prices = [4, 9, 0, 4, 10]. To get maximum profits you will have to buy on day 0 and sell on day 1 to make a profit of 5, and then you have to buy on day 3  and sell on day 4 to make the total profit of 11. Hence the maximum profit is 11.


Detailed explanation ( Input/output format, Notes, Images )
Sample Input 1:
4
1 2 3 4


Expected Answer:
3


Output on console:
3


Explanation:
For this test case, prices = [1, 2, 3, 4]. To get the maximum profit you have to buy the stock on day 0 and sell on day 3 to get the maximum profit of 4. Hence the answer is 4.


Sample Input 2:
3
5 4 3


Expected Answer:
0


Output on console:
0


Expected Time Complexity:
Try to solve this in O(n).


Constraints:
1 <= n <= 10^5
1 <= prices[i] <= 10^6

Time Limit: 1 sec
"""


def stockProfit(values: List[int]) -> int:
    # Write your code here.
    n= len(values)
    dp= [[0]*2 for _ in range(n+2)]
    for ind in range(n-1,-1,-1):
        for buy in range(2):
            if buy:
                dp[ind][buy]=max(-values[ind]+dp[ind+1][0] ,dp[ind+1][1])
            else:
                dp[ind][buy] = max(values[ind] + dp[ind+2][1] , dp[ind+1][0])
    return dp[0][1]





from typing import List

def solve(ind , buy , values , n , dp):
    if ind>=n:
        return 0

    if dp[ind][buy]!=-1:
        return dp[ind][buy]

    if buy==True:
        profit = max ( -values[ind] + solve(ind+1 , False , values , n , dp),
                     0 + solve(ind+1 , buy , values , n,dp))
    else:
        profit = max (values[ind] + solve(ind+2 , True , values , n,dp),
                    0+solve(ind+1 , buy , values , n,dp))

    dp[ind][buy] = profit
    return dp[ind][buy]


def stockProfit(prices: List[int]) -> int:
    # Write your code here.
    n= len(prices)
    dp= [[-1]*2 for _ in range(n)]
    return solve(0,True,prices,n,dp)
