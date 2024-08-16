"""   
Problem statement

There is a frog on the '1st' step of an 'N' stairs long staircase. The frog wants to reach the 'Nth' stair. 'HEIGHT[i]' is the height of the '(i+1)th' stair.If Frog jumps from 'ith' to 'jth' stair, the energy lost in the jump is given by absolute value of ( HEIGHT[i-1] - HEIGHT[j-1] ). If the Frog is on 'ith' staircase, he can jump either to '(i+1)th' stair or to '(i+2)th' stair. Your task is to find the minimum total energy used by the frog to reach from '1st' stair to 'Nth' stair.

For Example
If the given ‘HEIGHT’ array is [10,20,30,10], the answer 20 as the frog can jump from 1st stair to 2nd stair (|20-10| = 10 energy lost) and then a jump from 2nd stair to last stair (|10-20| = 10 energy lost). So, the total energy lost is 20.
Detailed explanation ( Input/output format, Notes, Images )
Constraints:
1 <= T <= 10
1 <= N <= 100000.
1 <= HEIGHTS[i] <= 1000 .

Time limit: 1 sec
Sample Input 1:
2
4
10 20 30 10
3
10 50 10
Sample Output 1:
20
0
Explanation of sample input 1:
For the first test case,
The frog can jump from 1st stair to 2nd stair (|20-10| = 10 energy lost).
Then a jump from the 2nd stair to the last stair (|10-20| = 10 energy lost).
So, the total energy lost is 20 which is the minimum. 
Hence, the answer is 20.

For the second test case:
The frog can jump from 1st stair to 3rd stair (|10-10| = 0 energy lost).
So, the total energy lost is 0 which is the minimum. 
Hence, the answer is 0.
Sample Input 2:
2
8
7 4 4 2 6 6 3 4 
6
4 8 3 10 4 4 
Sample Output 2:
7
2


Hints:
1. Think about all the possibilities at each stair.
2. Using recursion, try to divide the problem into subproblems and calculate the answer for each subproblem only once - store it for reusing in the future.
3. The above can also be done iteratively.




"""






from os import *
from sys import *
from collections import *
from math import *

from typing import *

def solve(dp,n,arr):
    if(n==0):
        return 0
    if n==1:
        return  abs(arr[1]-arr[0])
    if dp[n]!=-1:
        return dp[n]
    one_step=abs(arr[n]-arr[n-1])+solve(dp,n-1,arr)
    two_step=abs(arr[n]-arr[n-2])+solve(dp,n-2,arr)
    dp[n]= min(one_step , two_step) 
    return dp[n]

  
def frogJump(n: int, heights: List[int]) -> int:

    # Write your code here.
    dp=[-1]*n
    return solve(dp,n-1,heights)
    

# tabulation 


def frogJump(n: int, heights: List[int]) -> int:

    # Write your code here.
    dp=[-1]*n
    dp[0]=0
    dp[1]=abs(heights[1]-heights[0])

    for i in range(2,n,1):
        one_step=abs (heights[i]-heights[i-1])      +dp[i-1]
        two_step=abs( heights[i]-heights[i-2]  )  +dp[i-2]
        dp[i] = min(one_step , two_step)
    return dp[n-1]
