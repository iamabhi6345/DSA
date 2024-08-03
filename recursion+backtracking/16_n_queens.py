class Solution:
    
    def solve(self ,n, bd, ans, col, left, ud, ld ):
        if col==n:
            ans.append(bd.copy())
            return

        for row in range(n):
            if(left[row]==0) and(ld[row+col]==0) and (ud[n-1+col-row]==0):
                bd[row]=bd[row][:col]+"Q"+bd[row][col+1:]
                left[row]=1
                ud[n-1+col-row]=1
                ld[row+col]=1
                self.solve(n,bd,ans,col+1,left,ud,ld)
                bd[row]=bd[row][:col]+"."+bd[row][col+1:]
                left[row]=0
                ld[row+col]=0
                ud[n-1+col-row]=0

        

    def solveNQueens(self, n: int) -> List[List[str]]:
        left=[0]*n
        ud = [0]*(2*n  - 1)
        ld=[0]*(2*n -1)

        bd=["."*n for _ in range(n)]
        ans=list()
        self.solve(n,bd,ans,0,left,ud,ld)
        return ans
