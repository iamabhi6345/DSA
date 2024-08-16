from os import *
from sys import *
from collections import *
from math import *

def lcs_dp(s1 , s2 , n1 , n2 ):

    dp=[[0]*(n2+1) for _ in range(n1+1)]

    for i in range(1,n1+1):
        for j in range(1,n2+1):
            if s1[i-1]==s2[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j]  , dp[i][j-1])
    return dp
    

def shortestSupersequence(a: str, b: str) -> str:
	# Write your code here.
    n1= len(a)
    n2=len(b)
    dp=lcs_dp(a , b , n1 , n2)

    i = n1
    j=n2
    ans=""
    while(i>0 and j>0):
        if (a[i-1]==b[j-1]):
            ans=a[i-1]+ans
            i-=1
            j-=1

        elif (dp[i-1][j] > dp[i][j-1]):
            ans=a[i-1]+ans
            i-=1
        else:
            ans=b[j-1]+ans
            j-=1
    if (i>0):
        ans=a[:i] + ans
    if (j >0):
        ans=b[:j] + ans
        

    return ans
