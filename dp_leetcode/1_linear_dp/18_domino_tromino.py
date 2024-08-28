# https://www.youtube.com/watch?v=Iwmn-gFL3c0/
class Solution:
    def numTilings(self, n: int) -> int:
        m= int(1e9+7)
        dp = [0]*(n+1)
        if n<=2:
            return n
        dp[1]=1
        dp[2]=2
        dp[3]=5

        for i in range(4,n+1):
            dp[i]=(2*dp[i-1] + dp[i-3])%m
        return dp[n]