
class Solution:
    

    def solve(self ,i , j , dp , nr , nc):
        
        if(i==(nr-1)  and j ==(nc-1)):
            return 1
        elif (i>=nr  or j>=nc):
            return 0

        elif dp[i][j]!=-1:
            return dp[i][j]

        l= self.solve(i+1 , j , dp , nr , nc)
        r = self.solve(i,j+1 , dp , nr , nc)

        dp[i][j]=l+r
        return dp[i][j]





    def uniquePaths(self, nr: int, nc: int) -> int:
        dp=[[-1]*nc for _ in range(nr)]
        return self.solve(0,0,dp,nr,nc)
    
    
    
    


#   tabulation

class Solution:
    
    def uniquePaths(self, nr: int, nc: int) -> int:
        if (nr==1  or nc ==1):
            return 1
        dp=[[1]*nc for _ in range(nr)]

        for i in range(1,nr,1):
            for j in range(1,nc ,1):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        return dp[nr-1][nc-1]