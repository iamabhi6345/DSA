from os import *
from sys import *
from collections import *
from math import *
import sys
## Read input as specified in the question.
## Print output as specified in the question.


def solve( ind , tar , dp , w , v ):
    if (ind==0):
        if (w[0] <= tar):
            return v[0]
        return 0


    if dp[ind][tar]!=-1:
        return dp[ind][tar]
    
    nottake = solve( ind-1 , tar , dp , w , v)
    take=  -1e9
    if(w[ind]<=tar):
        take = v[ind] + solve( ind-1 , tar-w[ind] , dp , w , v)
    
    dp[ind][tar] = max(take , nottake)
    return dp[ind][tar]


t= int(sys.stdin.readline().rstrip())
for _ in range(t):
    n= int(sys.stdin.readline().rstrip())
    w= list(map(int,sys.stdin.readline().rstrip().split(" ")))
    v= list(map(int,sys.stdin.readline().rstrip().split(" ")))
    lim = int(sys.stdin.readline().rstrip())

    dp = [[-1]*(lim+1) for _ in range(n)]
    for i in range(w[0],lim):
        dp[0][i]=v[0]
    print(solve( n-1 , lim, dp, w, v ))

