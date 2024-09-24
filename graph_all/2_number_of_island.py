"""
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

 

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
         

"""

class Solution:
    def dfs(self , i , j , vis , grid):
        R =len(grid)
        C= len(grid[0])
        vis[i][j]=True
        drow=[-1 , 0 , 1 , 0]
        dcol = [0,1,0,-1]

        st=[(i,j)]
        while st:
            r,c = st.pop()
            for i in range(4):
                nrow = r + drow[i]
                ncol = c + dcol[i]

                if 0<=nrow<R and 0<=ncol<C and vis[nrow][ncol]==False and grid[nrow][ncol]=='1':
                    st.append((nrow,ncol))
                    vis[nrow][ncol]=True

    def numIslands(self, grid: List[List[str]]) -> int:
        r = len(grid)
        c = len(grid[0])
        vis = [[False]*c for _ in range(r)]
        ans=0

        for i in range(r):
            for j in range(c):
                if vis[i][j]==False and grid[i][j]=='1':
                    self.dfs(i,j,vis,grid)
                    ans+=1
        return ans
