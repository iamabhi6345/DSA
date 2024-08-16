from os import *
from sys import *
from collections import *
from math import *

from typing import List

def solve(ind , tar , dp , arr):
    if (ind == 0):
        if (tar == 0 and arr[0] == 0):
            return 2
        if(tar == 0  or tar == arr[0]):
            return 1
        return 0
    
    if dp[ind][tar]!=-1:
        return dp[ind][tar]
    
    nottake = solve(ind-1, tar , dp , arr)
    take =0
    if (arr[ind] <= tar):
        take = solve(ind -1 , tar-arr[ind] , dp , arr)
    
    dp[ind][tar]=take + nottake
    return dp[ind][tar]



def countPartitions(n: int, d: int, arr: List[int]) -> int:
    # write your code here\
    total = sum(arr)
    if total-d <0:
        return 0
    if (total-d) %2==1:
        return 0
    
    s2= ( total - d) //2

    dp= [[-1]*(s2+1) for _ in range(n)]
    return solve (n-1 , s2 , dp , arr)

