
""" 

Given a grid of dimension nxm where each cell in the grid can have values 0, 1 or 2
which has the following meaning:
0 : Empty cell
1 : Cells have fresh oranges
2 : Cells have rotten oranges

We have to determine what is the earliest time after which all the oranges are 
rotten. A rotten orange at index [i,j] can rot other fresh orange at 
indexes [i-1,j], [i+1,j], [i,j-1], [i,j+1] (up, down, left and right) in unit time. 
 

Example 1:

Input: grid = {{0,1,2},{0,1,2},{2,1,1}}
Output: 1
Explanation: The grid is-
0 1 2
0 1 2
2 1 1
Oranges at positions (0,2), (1,2), (2,0)
will rot oranges at (0,1), (1,1), (2,2) and 
(2,1) in unit time.
Example 2:

Input: grid = {{2,2,0,1}}
Output: -1
Explanation: The grid is-
2 2 0 1
Oranges at (0,0) and (0,1) can't rot orange at
(0,3).
 

Your Task:
You don't need to read or print anything, Your task is to complete the function 
orangesRotting() which takes grid as input parameter and returns the minimum time 
to rot all the fresh oranges. If not possible returns -1.

"""



from collections import deque

class Solution:

    def orangesRotting(self, grid):

        nr= len(grid)
        nc= len(grid[0])
        vis = [[0]*nc for _ in range(nr)]
        ans_time=0
        count_fresh=0

        drow=[-1,0,1,0]
        dcol=[0,1,0,-1]

        dq=deque()

        for i in range(nr):
            for j in range(nc):
                if grid[i][j]==2:
                    dq.append((i,j,0))
                    vis[i][j]=2

                elif grid[i][j]==1:
                    count_fresh+=1

        while dq:
            r,c,t = dq.popleft()
            ans_time=max(ans_time,t)

            for i in range(4):
                nrow = r + drow[i]
                ncol = c + dcol[i]

                if (0<=nrow<nr and 0<=ncol<nc and vis[nrow][ncol]==0 and 
                         grid[nrow][ncol]==1):
                             dq.append((nrow,ncol,t+1))
                             vis[nrow][ncol]=2
                             count_fresh-=1

        if count_fresh!=0:
            return -1

        return ans_time  

