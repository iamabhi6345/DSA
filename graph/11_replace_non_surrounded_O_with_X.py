""" 
Given a matrix mat of size N x M where every element is either 'O' or 'X'. Replace all 'O' or a group of 'O' 
with 'X' that are surrounded by 'X'.

A 'O' (or a set of 'O') is considered to be surrounded by 'X' if there are 'X' at locations just below, just
above, just left and just right of it.

Example 1:

Input: 
n = 5, m = 4
mat = {{'X', 'X', 'X', 'X'}, 
       {'X', 'O', 'X', 'X'}, 
       {'X', 'O', 'O', 'X'}, 
       {'X', 'O', 'X', 'X'}, 
       {'X', 'X', 'O', 'O'}}
Output: 
ans = {{'X', 'X', 'X', 'X'}, 
       {'X', 'X', 'X', 'X'}, 
       {'X', 'X', 'X', 'X'}, 
       {'X', 'X', 'X', 'X'}, 
       {'X', 'X', 'O', 'O'}}
Explanation: 
Following the rule the above matrix is the resultant matrix. 
Example 2:

 

Input: 
n = 5, m = 4
mat = {{'X', 'O', 'X', 'X'}, 
       {'X', 'O', 'X', 'X'}, 
       {'X', 'O', 'O', 'X'}, 
       {'X', 'O', 'X', 'X'}, 
       {'X', 'X', 'O', 'O'}}
Output: 
ans = {{'X', 'O', 'X', 'X'}, 
       {'X', 'O', 'X', 'X'}, 
       {'X', 'O', 'O', 'X'}, 
       {'X', 'O', 'X', 'X'}, 
       {'X', 'X', 'O', 'O'}}
Explanation: 
Following the rule the above matrix is the resultant matrix.
Your Task:
You do not need to read input or print anything. Your task is to complete the function fill() which takes N, M
and mat as input parameters ad returns a 2D array representing the resultant matrix.

Expected Time Complexity: O(n*m)
Expected Auxiliary Space: O(n*m)

Constraints:
1 ≤ n, m ≤ 500


"""




class Solution:
    def dfs(self,sr,sc,mat,vis,nr,nc):
        stack=[]
        stack.append((sr,sc))
        drow=[-1,0,1,0]
        dcol=[0,1,0,-1]
    
        while stack:
            r,c=stack.pop()
            vis[r][c]=1
            
            for i in range(4):
                nrow=r+drow[i]
                ncol=c+dcol[i]
                
                if(0<=nrow<nr and 0<=ncol<nc and mat[nrow][ncol]=='O'
                        and not vis[nrow][ncol]):
                    stack.append((nrow,ncol))
                    
                    
  
    def fill(self, nr, nc, mat):
        # code here
        vis=[[0]*nc for _ in range(nr)]
        
        
 
        for j in range(nc):
            if(mat[0][j]=="O" and not vis[0][j] ):
                self.dfs(0,j,mat,vis,nr,nc)
            if(mat[nr-1][j]=='O' and not vis[nr-1][j]):
                self.dfs(nr-1,j,mat,vis,nr,nc)
        
        for i in range(nr):
            if(mat[i][0]=='O' and not vis[i][0]):
                self.dfs(i,0,mat,vis,nr,nc)
            if(mat[i][nc-1]=='O' and not vis[i][nc-1]):
                self.dfs(i,nc-1,mat,vis,nr,nc)
        
        ans=[['X']*nc for _ in range(nr)]
        for i in range(nr):
            for j in range(nc):
                if(vis[i][j]==1):
                    ans[i][j]='O'
        return ans
    