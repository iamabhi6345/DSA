from os import *
from sys import *
from collections import *
from math import *

mod = 1e9+7
def solve(dp,n):
    
    if n<=1:
        return 1 
    
    if dp[n]!=-1:
        return dp[n]
    one_step=solve(dp,n-1) %mod
    two_step=solve(dp,n-2) %mod
    dp[n]=(one_step + two_step) %mod
    return int(dp[n])

def countDistinctWays(nStairs: int) -> int:
    #  Write your code here.
    dp=[-1]*(nStairs+1)
    return solve(dp,nStairs)



# tabulation
from os import *
from sys import *
from collections import *
from math import *

mod = 1e9+7


def countDistinctWays1(nStairs: int) -> int:
    #  Write your code here.
    if nStairs<=1:
        return 1
    dp=[-1]*(nStairs+1)
    dp[0]=1
    dp[1]=1
    for i in range(2,nStairs+1,1):
        dp[i]=int((dp[i-1]+dp[i-2])%mod)
    return dp[nStairs]

# do space optimization 

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    num_cases = int(data[0])
    results = []
    
    for i in range(1, num_cases + 1):
        nStairs = int(data[i])
        results.append(countDistinctWays(nStairs))
    
    for result in results:
        print(result)  

if __name__ == "__main__":
    main()
    
# python 2_count_ways_to_reach_n_stairs.py < 2_input.txt 