"""   
Problem statement
You are given an array ‘ARR’ of ‘N’ integers and a target number, ‘TARGET’. Your task is to build an expression out of an array by adding one of the symbols '+' and '-' before each integer in an array, and then by concatenating all the integers, you want to achieve a target. You have to return the number of ways the target can be achieved.

For Example :
You are given the array ‘ARR’ = [1, 1, 1, 1, 1], ‘TARGET’ = 3. The number of ways this target can be achieved is:
1. -1 + 1 + 1 + 1 + 1 = 3
2. +1 - 1 + 1 + 1 + 1 = 3
3. +1 + 1 - 1 + 1 + 1 = 3
4. +1 + 1 + 1 - 1 + 1 = 3
5. +1 + 1 + 1 + 1 - 1 = 3
These are the 5 ways to make. Hence the answer is 5.
Detailed explanation ( Input/output format, Notes, Images )
Constraints :
1 <= T <= 10
1 <= N <= 25
-1000 <= TARGET <= 1000
0 <= ARR[i] <= 1000

Time Limit: 1 sec
Note :
You do not need to print anything. It has already been taken care of. Just implement the given function.
Sample input 1 :
2
5 3
1 1 1 1 1
4 3
1 2 3 1
Sample Output 2 :
5
2
Explanation For Sample Input 1 :
For the first test case, ‘ARR’ = [1, 1, 1, 1, 1], ‘TARGET’ = 3. The number of ways this target can be achieved is:
1. -1 + 1 + 1 + 1 + 1 = 3
2. +1 - 1 + 1 + 1 + 1 = 3
3. +1 + 1 - 1 + 1 + 1 = 3
4. +1 + 1 + 1 - 1 + 1 = 3
5. +1 + 1 + 1 + 1 - 1 = 3
These are the 5 ways to get the target. Hence the answer is 5.

For the second test case, ‘ARR’ = [1, 2, 3, 1]. ‘TARGET’ = 3, The number of ways this target can be achieved is:
1. +1 - 2 + 1 + 3 = 3
2. -1 + 2 - 1 + 3 = 3
These are the 3 ways to get the target. Hence the answer is 2.
Sample Input 2 :
2
3 2
1 2 3
2 0
1 1
Sample Output 2 :
1
2


"""






from collections import *
from math import *

from typing import List

def solve1(ind , tar , dp , arr):
    if ind ==0:
        if tar==0 and arr[0]==0:
            return 2
        if tar==0 or tar==arr[0]:
            return 1
        else:
            return 0
    
    if dp[ind][tar]!=-1:
        return dp[ind][tar]
    
    nottake = solve1(ind-1 , tar , dp , arr)
    take =0
    if (arr[ind]<=tar):
        take = solve1(ind-1 , tar-arr[ind],dp,arr)
    
    dp[ind][tar] = take + nottake
    return dp[ind][tar]



def solve(arr , k ):
    total = sum(arr)
    nr=len(arr)
    nc=k+1

    dp=[[0]*nc for _ in range(nr)]

    if arr[0]==0:
        dp[0][0]=2
    else:
        dp[0][0]=1
    
    
    if (arr[0]<=k   and arr[0]!=0):
        dp[0][arr[0]]=1

    for i in range(1, nr):
        for j in range(0,nc):
            nottaken = dp[i-1][j]
            taken= 0

            if ( arr[i]<=j):
                taken = dp[i-1][j-arr[i]]

            dp[i][j] = taken + nottaken 

    return dp 



def targetSum(arr: List[int], target: int) -> int:
    
    nr = len(arr)
    
    total = sum(arr)
    if total-target <0:
        return 0
    if ((total-target) %2 ==1):
        return 0
    k = (total - target)//2
    
    return solve( arr , k)[nr-1][k]

    dp=[[-1]*(k+1) for _ in range(nr)]
    return solve1(nr-1 , k , dp , arr)
