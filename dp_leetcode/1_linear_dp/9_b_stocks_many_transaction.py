""" 
Problem statement
You have been given stock values/prices for N number of days. Every i-th day signifies the price of a stock on that day. Your task is to find the maximum profit which you can make by buying and selling the stocks.

 Note :
You may make as many transactions as you want but can not have more than one transaction at a time i.e, if you have the stock, you need to sell it first, and then only you can buy it again.
Detailed explanation ( Input/output format, Notes, Images )
Constraints :
1 <= t <= 10^2
0 <= N <= 10^5
Time Limit: 1 sec
Sample Input 1 :
1
7
1 2 3 4 5 6 7
Sample Output 1 :
6
Explanation :
We can make the maximum profit by buying the stock on the first day and selling it on the last day.
Sample Input 2 :
1
7
7 6 5 4 3 2 1
Sample Output 2 :
0
Explanation :
We can make the maximum profit by not buying the stock.
"""

""" 
 dp[ind][buy]--->if buy=True then we can buy at index=ind
"""

def getMaximumProfit(values, n) :
    	#Your code goes here
    n = len(values)
    dp= [[0]*2 for _ in range(n+1)]

    for ind in range(n-1,-1,-1):
        for buy in range(2):
            if buy:
                dp[ind][buy]=max(-values[ind]+dp[ind+1][0] ,dp[ind+1][1])
            else:
                dp[ind][buy] = max(values[ind] + dp[ind+1][1] , dp[ind+1][0])


    return dp[0][1]



def solve(ind , buy , values , n , dp):
    if ind==n:
        return 0
    
    if dp[ind][buy]!=-1:
        return dp[ind][buy]
    
    if buy==True:
        profit = max ( -values[ind] + solve(ind+1 , False , values , n , dp),
                     0 + solve(ind+1 , buy , values , n,dp))
    else:
        profit = max (values[ind] + solve(ind+1 , True , values , n,dp),
                    0+solve(ind+1 , buy , values , n,dp))
    
    dp[ind][buy] = profit
    return dp[ind][buy]




def getMaximumProfit(values, n) :
    #Your code goes here
    sum=0

    for i in range(1,len(values)):
        sum+=(values[i]-values[i-1]) if values[i]>values[i-1] else 0
    return sum

