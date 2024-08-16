""" 

Given a grid of size n*m (n is the number of rows and m is the number of columns in 
the grid) consisting of '0's (Water) and '1's(Land). Find the number of islands.

Note: An island is either surrounded by water or boundary of grid and is formed by 
connecting adjacent lands horizontally or vertically or diagonally i.e., in all 8 
directions.

Example 1:

Input:
grid = {{0,1},{1,0},{1,1},{1,0}}
Output:
1
Explanation:
The grid is-
0 1
1 0
1 1
1 0
All lands are connected.
Example 2:

Input:
grid = {{0,1,1,1,0,0,0},{0,0,1,1,0,1,0}}
Output:
2
Expanation:
The grid is-
0 1 1 1 0 0 0
0 0 1 1 0 1 0 
There are two islands :- one is colored in blue 
and other in orange.
Your Task:
You don't need to read or print anything. Your task is to complete the function 
numIslands() which takes the grid as an input parameter and returns the total number
of islands.

Expected Time Complexity: O(n*m)
Expected Space Complexity: O(n*m)

Constraints:
1 ≤ n, m ≤ 500

"""

#User function Template for python3

import sys
sys.setrecursionlimit(10**8)
class Solution:
    
    def __dfs(self , sr , sc , grid , vis ):
        nr = len(grid)
        nc = len(grid[0])
        
        stack = []
        stack.append((sr,sc))
        vis[sr][sc]=True
        
        drow= [-1,-1,-1,0,1,1,1,0]
        dcol= [-1,0,1,1,1,0,-1,-1]
        
        
        while stack:
            r , c = stack.pop()
            for i in range(8):
                nrow = r+ drow[i]
                ncol= c+ dcol[i]
                
                if(0<=nrow<nr and 0<=ncol<nc and grid[nrow][ncol]==1 and 
                        vis[nrow][ncol]==False):
                            stack.append((nrow,ncol))
                            vis[nrow][ncol]=True

        return



    def numIslands(self,grid):
        #code here
        nr = len(grid)
        nc= len(grid[0])
        
        vis=[[False]*nc for _ in range(nr)]
        
        count=0
        
        for i in range(nr):
            for j in range(nc):
                if(grid[i][j]==1 and vis[i][j]==False ):
                    self.__dfs(i,j,grid,vis)
                    count+=1
        
        return count
        
 