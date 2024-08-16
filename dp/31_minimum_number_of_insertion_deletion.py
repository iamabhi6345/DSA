 
def canYouMake(s1: str, s2: str) -> int:
    # write your code here
    n1 = len(s1)
    n2 = len(s2)
  
    dp = [[0]*(n2+1) for _ in range(n1+1)]
 
    for i in range(1,n1+1):
        for j in range(1 , n2+1):
            if s1[i-1]==s2[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
 
            else:
                dp[i][j] = max ( dp[i-1][j]  , dp[i][j-1])
    lcs = dp[n1][n2]
    return (n1 - lcs + n2- lcs)
 
 