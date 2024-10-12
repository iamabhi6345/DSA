""" 

https://atcoder.jp/contests/dp/tasks/dp_b
"""

import sys

# def solve(ind, height, dp, k):
#     if (ind==0):
#         return 0
#     if dp[ind]!=-1:
#         return dp[ind]
#     minstep=sys.maxsize
#     for i in range(1,k+1):
#         if(ind-i>=0):
#             tmp=abs(height[ind]-height[ind-i]) + solve(ind-i,height,dp,k)
#             minstep = min(minstep,tmp)
#     dp[ind]=minstep
#     return dp[ind]


# def kjumps(arr,k):
#     n=len(arr)
#     dp=[-1]*n
#     return solve(n-1,arr,dp,k)


# print(kjumps([40, 10, 20 ,70, 80, 10 ,20, 70, 80, 60],4))
# print(kjumps([30, 10, 60, 10, 60, 50],2))
# print(kjumps([10 ,30 ,40, 50, 20],3))
# print(kjumps([10 ,20,10],1))
# print(kjumps([10 ,0],100))

                





#  tabulation


import sys
n ,k = map(int , sys.stdin.readline().strip().split(" "))
arr = list(map(int , sys.stdin.readline().strip().split(" ")))

dp=[sys.maxsize]*n
dp[0]=0

for i in range(1,n):
  for j in range(1,k+1):
    if i-j>=0:
      dp[i]=min(dp[i],    abs((arr[i]-arr[i-j])) + dp[i-j])

print(dp[n-1])