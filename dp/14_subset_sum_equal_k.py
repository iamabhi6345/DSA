"""   

Problem statement
You are given an array/list ‘ARR’ of ‘N’ positive integers and an integer ‘K’. Your task is to check if there exists a subset in ‘ARR’ with a sum equal to ‘K’.

Note: Return true if there exists a subset with sum equal to ‘K’. Otherwise, return false.

For Example :
If ‘ARR’ is {1,2,3,4} and ‘K’ = 4, then there exists 2 subsets with sum = 4. These are {1,3} and {4}. Hence, return true.
Detailed explanation ( Input/output format, Notes, Images )
Constraints:
1 <= T <= 5
1 <= N <= 10^3
0 <= ARR[i] <= 10^9
0 <= K <= 10^3

Time Limit: 1 sec
Sample Input 1:
2
4 5
4 3 2 1
5 4
2 5 1 6 7
Sample Output 1:
true
false
Explanation For Sample Input 1:
In example 1, ‘ARR’ is {4,3,2,1} and ‘K’ = 5. There exist 2 subsets with sum = 5. These are {4,1} and {3,2}. Hence, return true.
In example 2, ‘ARR’ is {2,5,1,6,7} and ‘K’ = 4. There are no subsets with sum = 4. Hence, return false.
Sample Input 2:
2
4 4
6 1 2 1
5 6
1 7 2 9 10
Sample Output 2:
true
false
Explanation For Sample Input 2:
In example 1, ‘ARR’ is {6,1,2,1} and ‘K’ = 4. There exist 1 subset with sum = 4. That is {1,2,1}. Hence, return true.
In example 2, ‘ARR’ is {1,7,2,9,10} and ‘K’ = 6. There are no subsets with sum = 6. Hence, return false.


Hints:
1. Can you find every possible subset of ‘ARR’ and check if its sum is equal to ‘K’?
2. Can you use dynamic programming and use the previously calculated result to calculate the new result?
3. Try to use a recursive approach followed by memoization by including both index and sum we can form. 

"""


from os import *
from sys import *
from collections import *
from math import *

def solve(ind , tar , arr ,dp ):
    if tar==0:
        return True

    if ind==0:
        return arr[ind]==tar

    if dp[ind][tar]!=-1:
        return dp[ind][tar]
    
    taken =False
    if (tar >= arr[ind]):
            taken =  solve(ind-1,tar-arr[ind],arr,dp)
    
    nottaken= solve(ind-1,tar,arr,dp)
    dp[ind][tar] = taken or nottaken
    return dp[ind][tar]

def subsetSumToK(n, k, arr):

    dp=[[-1]*(k+1) for _ in range(n)]
    return solve(n-1,k,arr,dp)







# tabulation



from os import *
from sys import *
from collections import *
from math import *

def subsetSumToK(n, k, arr):

    dp = [[False]*(k+1) for _ in range(n)]

    for i in range(n):
        dp[i][0]=True

    if (arr[0]<=k):
        dp[0][arr[0]]=True

    for i in range(1,n):
        for j in range(1,k+1):
            taken=False
            if arr[i]<=j:
                taken=dp[i-1][j-arr[i]]
            
            nottaken = dp[i-1][j]

            dp[i][j]=taken or nottaken

    return dp[n-1][k]





