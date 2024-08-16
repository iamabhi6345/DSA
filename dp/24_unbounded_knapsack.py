from typing import List

def solve(ind , tar , dp , w , p):
    if (ind==0):
        if (w[0]<=tar):
            return (tar//w[0])*p[0]
        else:
            return 0
    
    if dp[ind][tar]!=-1:
        return dp[ind][tar]

    nottake = solve(ind-1 , tar , dp , w ,p)
    take =0
    if (w[ind]<=tar):
        take = p[ind] + solve(ind , tar-w[ind] , dp , w , p)
    dp[ind][tar]= max(take , nottake) 
    return dp[ind][tar] 


def unboundedKnapsack(n: int, w: int, profit: List[int], weight: List[int]) -> int:
    # write your code here
    dp=[[-1]*(w+1) for _ in range(n)]
    return solve( n-1 , w , dp , weight , profit )
    