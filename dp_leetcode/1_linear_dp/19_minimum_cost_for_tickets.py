"""  
?????????????????????https://www.youtube.com/watch?v=YrCTd8p5-bY

You have planned some train traveling one year in advance. The days of the year in which you will travel are given as an integer array days. Each day is an integer from 1 to 365.

Train tickets are sold in three different ways:

a 1-day pass is sold for costs[0] dollars,
a 7-day pass is sold for costs[1] dollars, and
a 30-day pass is sold for costs[2] dollars.
The passes allow that many days of consecutive travel.

For example, if we get a 7-day pass on day 2, then we can travel for 7 days: 2, 3, 4, 5, 6, 7, and 8.
Return the minimum number of dollars you need to travel every day in the given list of days.

 

Example 1:

Input: days = [1,4,6,7,8,20], costs = [2,7,15]
Output: 11
Explanation: For example, here is one way to buy passes that lets you travel your travel plan:
On day 1, you bought a 1-day pass for costs[0] = $2, which covered day 1.
On day 3, you bought a 7-day pass for costs[1] = $7, which covered days 3, 4, ..., 9.
On day 20, you bought a 1-day pass for costs[0] = $2, which covered day 20.
In total, you spent $11 and covered all the days of your travel.
Example 2:

Input: days = [1,2,3,4,5,6,7,8,9,10,30,31], costs = [2,7,15]
Output: 17
Explanation: For example, here is one way to buy passes that lets you travel your travel plan:
On day 1, you bought a 30-day pass for costs[2] = $15 which covered days 1, 2, ..., 30.
On day 31, you bought a 1-day pass for costs[0] = $2 which covered day 31.
In total, you spent $17 and covered all the days of your travel.
 

Constraints:

1 <= days.length <= 365
1 <= days[i] <= 365
days is in strictly increasing order.
costs.length == 3
1 <= costs[i] <= 1000

"""


class Solution:
    def mincostTickets(self, days: List[int], cost: List[int]) -> int:
        dp = [int(1e8)]*366
        dp[0]=0

        last=days[-1]
        for i in range(1,last+1):
            if i not in days:
                dp[i]=dp[i-1]
                continue

            p1 = cost[0]+dp[max(0,i-1)]
            p7 = cost[1]+dp[max(0,i-7)]
            p30= cost[2]+dp[max(0,i-30)]
            dp[i]=min(p1,min(p7,p30))
        return dp[last] 





class Solution:
    def solve(self , ind , dp , days , cost):
        if ind==len(days):
            return 0
        if dp[ind]!=-1:
            return dp[ind]
        
        # 1 day wala cost
        p1 = cost[0]+ self.solve(ind+1 , dp , days , cost)

        #  7 days wala cost
        i=ind
        while(i < len(days) and days[i]< days[ind]+7):
            i+=1
        p7 = cost[1] + self.solve(i , dp , days , cost)

        #  30 days wala cots
        j= ind
        while(j<len(days) and days[j]<days[ind]+30):
            j+=1
        p30 = cost[2]+self.solve(j , dp , days , cost)

        dp[ind] = min(p1, min(p7,p30))
        return dp[ind]


    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = [-1]*len(days)
        return self.solve(0,dp,days,costs)
