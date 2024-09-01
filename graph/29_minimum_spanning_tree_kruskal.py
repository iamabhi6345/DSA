#User function Template for python3
from typing import List

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
    
    #Function to find sum of weights of edges of the Minimum Spanning Tree.
    def spanningTree(self, V: int, adj: List[List[int]]) -> int:
        #code here
        edge=[]
        for u in range(V):
            for v in adj[u]:
                if u<v[0]:
                    nextnode =v[0]
                    wt=v[1]
                    node=u
                    edge.append((wt,node,nextnode))
        edge.sort()
        ds = DisjointSet(V)
        ans=0
        
        for wt , u , v in edge:
            
            if ds.findUPar(u)!=ds.findUPar(v):
                # ds.union_by_rank(u,v)
                ds.union_by_size(u,v)
                ans+=wt
        
        return ans
                

if __name__ == "__main__":
    V = 5
    edges = [[0, 1, 2], [0, 2, 1], [1, 2, 1], [2, 3, 2], [3, 4, 1], [4, 2, 2]]
    adj = [[] for _ in range(V)]
    for u, v, weight in edges:
        adj[u].append([v, weight])
        adj[v].append([u, weight])

    obj = Solution()
    mst_weight = obj.spanningTree(V, adj)
    print("The sum of all the edge weights:", mst_weight)