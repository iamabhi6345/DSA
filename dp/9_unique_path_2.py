""" 
ou are given an m x n integer array grid. There is a robot initially located at the 
top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right 
corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at
any point in time.

An obstacle and space are marked as 1 or 0 respectively in grid. A path that the 
robot takes cannot include any square that is an obstacle.

Return the number of possible unique paths that the robot can take to reach the
bottom-right corner.


"""

class Solution:
    def solve(self,i , j , nr , nc , dp , mat):
        
        
        if(i==nr-1 and j==nc-1 ):
            return 1

        elif (i>=nr or j>=nc):
            return 0
        elif(i>=0 and j>=0 and mat[i][j]==1):
            return 0
        
        elif(dp[i][j]!=-1):
            return dp[i][j]
        
        r= self.solve(i , j+1 , nr,nc ,dp,mat)
        d = self.solve(i+1 , j , nr , nc , dp , mat)

        dp[i][j] = r+d
        return dp[i][j]



    def uniquePathsWithObstacles(self, mat: List[List[int]]) -> int:
        
        nr = len(mat)
        nc = len(mat[0])
        if mat[nr-1][nc-1]==1:
            return 0

        dp=[[-1]*nc for _ in range(nr)]


        return self.solve(0, 0, nr , nc , dp , mat)

    