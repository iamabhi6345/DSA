""" 
Given a binary grid of n*m. Find the distance of the nearest 1 in the grid for each cell.
The distance is calculated as |i1  - i2| + |j1 - j2|, where i1, j1 are the row number and column number of the current cell, and i2, j2 are the row number and column number of the nearest cell having value 1. There should be atleast one 1 in the grid.
 

Example 1:

Input: grid = {{0,1,1,0},{1,1,0,0},{0,0,1,1}}
Output: {{1,0,0,1},{0,0,1,1},{1,1,0,0}}
Explanation: The grid is-
0 1 1 0 
1 1 0 0 
0 0 1 1 
0's at (0,0), (0,3), (1,2), (1,3), (2,0) and
(2,1) are at a distance of 1 from 1's at (0,1),
(0,2), (0,2), (2,3), (1,0) and (1,1)
respectively.


Example 2:

Input: grid = {{1,0,1},{1,1,0},{1,0,0}}
Output: {{0,1,0},{0,0,1},{0,1,2}}
Explanation: The grid is-
1 0 1
1 1 0
1 0 0
0's at (0,1), (1,2), (2,1) and (2,2) are at a 
distance of 1, 1, 1 and 2 from 1's at (0,0),
(0,2), (2,0) and (1,1) respectively.


 

Yout Task:
You don't need to read or print anything, Your task is to complete the function nearest() which takes the grid as an input parameter and returns a matrix of the same dimensions where the value at index (i, j) in the resultant matrix signifies the minimum distance of 1 in the matrix from grid[i][j].
 

Expected Time Complexity: O(n*m)
Expected Auxiliary Space: O(n*m)

Constraints:
1 ≤ n, m ≤ 500


"""


from collections import deque

class Solution:

    #Function to find distance of nearest 1 in the grid for each cell.
	def nearest(self, grid):
		#Code here
		dq = deque()
		nr=len(grid)
		nc=len(grid[0])
		vis=[[0]*nc for _ in range(nr)]
		
		drow=[-1,0,1,0]
		dcol = [0,1,0,-1]
		
		for i in range(nr):
		    for j in range(nc):
		        if(grid[i][j]==1):
		            dq.append((i,j,0))
		
		while dq:
		    r,c,d= dq.popleft()
		    
		    for i in range(4):
		        nrow=r+drow[i]
		        ncol=c+dcol[i]
		        
		        if(0<=nrow<nr and 0<=ncol<nc and grid[nrow][ncol]==0
		                and vis[nrow][ncol]==0):
		                    vis[nrow][ncol]=d+1
		                    dq.append((nrow,ncol,d+1))
		                    
		return vis    
		           