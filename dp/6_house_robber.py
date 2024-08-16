from os import *
from sys import *
from collections import *
from math import *


def solve(nums):    
    # Write your code here.
    n=len(nums)
    if(n==1):
        return nums[0]
    dp=[-1]*n
    dp[0]=nums[0]
    dp[1]=max(nums[0],nums[1])

    for i in range(2,n,1):
        pick=nums[i]+dp[i-2]
        not_pick = dp[i-1]
        dp[i]=max(pick,not_pick)
    return dp[n-1]


def houseRobber(arr):
    # Write your function here.
    n=len(arr)
    if(n==1):
        return arr[0]
    tmp1 = arr[1:]
    tmp2=arr[0:n-1]
    return max ( solve(tmp1)  , solve(tmp2) )
import sys
n= int(sys.stdin.readline().rstrip())
arr=list(map(int , sys.stdin.readline().rstrip().split(" ")))
print(houseRobber(arr))

"""   
7
59 53 41 26 17 13 11
"""