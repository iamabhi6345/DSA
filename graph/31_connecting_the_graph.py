""" 
You are given a graph with n vertices (0 to n-1) and m edges. You can remove one edge from anywhere and add that edge between any two vertices in one operation. Find the minimum number of operations that will be required to connect the graph.
If it is not possible to connect the graph, return -1.

Example 1: 

Input:
n = 4
m = 3
Edges = [ [0, 1] , [0, 2] , [1, 2] ]
Output:
1
Explanation:
Remove edge between vertices 1 and 2 and add between vertices 1 and 3.
 

Example 2:

Input:
n = 6
m = 5
Edges = [ [0,1] , [0,2] , [0,3] , [1,2] , [1,3] ]
Output:
2
Explanation:
Remove edge between (1,2) and(0,3) and add edge between (1,4) and (3,5)
 
Your Task:
You don't need to read or print anything. Your task is to complete the function Solve() which takes an integer n denoting a number of vertices and a 2d matrix denoting the edges of a graph and returns the minimum number of operations to connect a graph.

Expected Time Complexity: O(m*n)
Expected Space Complexity: O(m*n)

Constraints:
1<=n<=105
0<=m<=102
1<=edge[i][0],edge[i][1]<=n-1

"""

class DisjointSet:
    def __init__(self , n):
        self.rank = [0]*(n+1)
        self.parent = [i for i in range(n+1)]
        self.size = [1]*(n+1)
    
    def findUPar(self , node):
        if node==self.parent[node]:
            return node
        self.parent[node] = self.findUPar(self.parent[node])
        return self.parent[node]
    
    def union_by_rank(self , u , v):
        upu= self.findUPar(u)
        upv= self.findUPar(v)
        
        if upu == upv:
            return

        if self.rank[upu] < self.rank[upv]:
            self.parent[upu]=upv
        elif self.rank[upv] <self.rank[upu]:
            self.parent[upv]=upu
        else:
            self.parent[upu]=upv
            self.rank[upv]+=1


    def union_by_size(self , u , v):
        upu=self.findUPar(u)
        upv=self.findUPar(v)

        if upu == upv:
            return

        if self.size[upu] < self.size[upv]:
            self.parent[upu]=upv
            self.size[upv]+=self.size[upu]
        
        else:
            self.parent[upv]=upu
            self.size[upu]+=self.size[upv]



class Solution:
    def Solve(self, n, adj):
        # Code here
        ds = DisjointSet(n)
        extraedge=0
        for u ,v in adj:
            if ds.findUPar(u)==ds.findUPar(v):
                extraedge+=1
            else:
                ds.union_by_rank(u,v)
        
        component=0
        
        for i in range(n):
            if ds.parent[i]==i:
                component+=1
        
        edgerequired = component-1
        if extraedge>=edgerequired:
            return edgerequired
        return -1


if __name__ == "__main__":
    V = 9
    edge = [[0, 1], [0, 2], [0, 3], [1, 2], [2, 3], [4, 5], [5, 6], [7, 8]]

    obj = Solution()
    ans = obj.Solve(V, edge)
    print("The number of operations needed:", ans)