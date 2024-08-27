"""
Problem statement
You have been given an array 'PRICES' consisting of 'N' integers where PRICES[i] denotes the price of a given stock on the i-th day. You are also given an integer 'K' denoting the number of possible transactions you can make.

Your task is to find the maximum profit in at most K transactions. A valid transaction involves buying a stock and then selling it.

Note
You can’t engage in multiple transactions simultaneously, i.e. you must sell the stock before rebuying it.
For Example
Input: N = 6 , PRICES = [3, 2, 6, 5, 0, 3] and K = 2.
Output: 7

Explanation : The optimal way to get maximum profit is to buy the stock on day 2(price = 2) and sell it on day 3(price = 6) and rebuy it on day 5(price = 0) and sell it on day 6(price = 3). The maximum profit will be (6 - 2) + (3 - 0) = 7.
Detailed explanation ( Input/output format, Notes, Images )
Constraints
1 <= T <= 100
1 <= N <= 5000
0 <= K <= N/2
0 <= ARR[i] <=10^5

Time Limit : 1 sec
Sample Input 1
2
5 2
8 5 1 3 10
4 2
10 8 6 2 
Sample Output 1
9
0
Explanation for Sample 1
Test Case 1: In this case, we can make a maximum of 2 transactions. The optimal way to get maximum profit is to make only 1 transaction, i.e., buy the stock on day 3 (price = 1) and sell it on day 5(price = 10). The profit will be 10 - 1 = 9.

Test Case 2: In the second test case, we can make a maximum of 2 transactions. The optimal way to get maximum profit is to make 0 transactions because the price of stock is continuously decreasing and we will have a loss if we buy and sell the stock.
Sample Input 2
2
4 0
2 6 5 2
4 2
1 2 3 5
Sample Output 2
0
4
"""

def maximumProfit(values, n, k):
    
    # Write your code here
    
    n = len(values)
    dp = [  [[0]*(k+1) for _ in range(2)]  for _ in range(n+1)]

    for ind in range(n-1,-1,-1):
        for buy in range(2):
            for cap in range(1,k+1):
                if buy:
                    dp[ind][buy][cap]=max(-values[ind]+dp[ind+1][0][cap],
                                dp[ind+1][1][cap])
                else:
                    dp[ind][buy][cap]=max(values[ind]+dp[ind+1][1][cap-1],
                            dp[ind+1][0][cap])
        
    return dp[0][1][k]

