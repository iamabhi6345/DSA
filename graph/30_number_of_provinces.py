
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
    def numProvinces(self, adj, V):
        # code here 
        ds = DisjointSet(V)
        for i in range(V):
            for j in range(V):
                if adj[i][j]==1:
                    ds.union_by_rank(i,j)
        count=0
        for i in range(V):
            if ds.parent[i]==i:
                count+=1
            
        return count
