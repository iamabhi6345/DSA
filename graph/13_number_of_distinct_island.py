""" 

Given a boolean 2D matrix grid of size n * m. You have to find the number of distinct islands where a group of connected 1s (horizontally or vertically) forms an island. Two islands are considered to be distinct if and only if one island is not equal to another (not rotated or reflected).

Example 1:

Input:
grid[][] = {{1, 1, 0, 0, 0},
            {1, 1, 0, 0, 0},
            {0, 0, 0, 1, 1},
            {0, 0, 0, 1, 1}}
Output:
1
Explanation:
grid[][] = {{1, 1, 0, 0, 0}, 
            {1, 1, 0, 0, 0}, 
            {0, 0, 0, 1, 1}, 
            {0, 0, 0, 1, 1}}
Same colored islands are equal.
We have 2 equal islands, so we 
have only 1 distinct island.

Example 2:

Input:
grid[][] = {{1, 1, 0, 1, 1},
            {1, 0, 0, 0, 0},
            {0, 0, 0, 0, 1},
            {1, 1, 0, 1, 1}}
Output:
3
Explanation:
grid[][] = {{1, 1, 0, 1, 1}, 
            {1, 0, 0, 0, 0}, 
            {0, 0, 0, 0, 1}, 
            {1, 1, 0, 1, 1}}
Same colored islands are equal.
We have 4 islands, but 2 of them
are equal, So we have 3 distinct islands.

Your Task:

You don't need to read or print anything. Your task is to complete the function countDistinctIslands() which takes the grid as an input parameter and returns the total number of distinct islands.

Expected Time Complexity: O(n * m)
Expected Space Complexity: O(n * m)

Constraints:
1 ≤ n, m ≤ 500
grid[i][j] == 0 or grid[i][j] == 1


"""


#User function Template for python3

import sys
from typing import List
sys.setrecursionlimit(10**8)
class Solution:
    
    def __dfs(self, sr,sc,grid,ans,vis):
        nr=len(grid)
        nc=len(grid[0])
        stack=[]
        stack.append((sr,sc))
        vis[sr][sc]=True
        drow=[-1,0,1,0]
        dcol=[0,1,0,-1]
        
        sti=sr
        stj=sc
        tmp=[]
        
        while stack:
            r,c = stack.pop()
            tmp.append((r-sti , c-stj))
            
            for i in range(4):
                nrow=r+drow[i]
                ncol=c+dcol[i]
                
                if(0<=nrow<nr and 0<=ncol<nc and grid[nrow][ncol]==1
                        and not vis[nrow][ncol]):
                            vis[nrow][ncol]=True
                            stack.append((nrow,ncol))
        ans.add(tuple(tmp))
            
            
    def countDistinctIslands(self, grid : List[List[int]]) -> int:
        # code here
        ans =set()
        nr=len(grid)
        nc=len(grid[0])
        
        vis=[[False]*nc for _ in range(nr)]
        for i in range(nr):
            for j in range(nc):
                if grid[i][j]==1 and vis[i][j]==False :
                    self.__dfs(i,j,grid,ans,vis)
        return len(ans)
                    
           