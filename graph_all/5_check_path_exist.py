""" 
There is a bi-directional graph with n vertices, where each vertex is labeled from 0 to n - 1 (inclusive). The edges in the graph are represented as a 2D integer array edges, where each edges[i] = [ui, vi] denotes a bi-directional edge between vertex ui and vertex vi. Every vertex pair is connected by at most one edge, and no vertex has an edge to itself.

You want to determine if there is a valid path that exists from vertex source to vertex destination.

Given edges and the integers n, source, and destination, return true if there is a valid path from source to destination, or false otherwise.

 

Example 1:


Input: n = 3, edges = [[0,1],[1,2],[2,0]], source = 0, destination = 2
Output: true
Explanation: There are two paths from vertex 0 to vertex 2:
- 0 → 1 → 2
- 0 → 2
Example 2:


Input: n = 6, edges = [[0,1],[0,2],[3,5],[5,4],[4,3]], source = 0, destination = 5
Output: false
Explanation: There is no path from vertex 0 to vertex 5.
 

Constraints:

1 <= n <= 2 * 105
0 <= edges.length <= 2 * 105
edges[i].length == 2
0 <= ui, vi <= n - 1
ui != vi
0 <= source, destination <= n - 1
There are no duplicate edges.
There are no self edges.
"""


class Solution:
    def dfs(self , start , end , adj , vis):
        vis[start]= True
        for node in adj[start]:
            if node==end:
                return True
            if vis[node]==False:
                if self.dfs(node,end,adj,vis):
                    return True
        return False
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if source == destination:
            return True
        adj =[ [] for _ in range(n)]

        for a , b in edges:
            adj[a].append(b)
            adj[b].append(a)
        vis= [False]*n
        return self.dfs(source , destination, adj , vis)

# ?????????????  method-2 using disjoint set

class DisjointSet:
    def __init__(self , n):
        self.size=[1]*(n+1)
        self.parent=[i for i in range(n+1)]
        self.rank = [0]*(n+1)
    def findUPar(self , node):
        if self.parent[node]==node:
            return node
        self.parent[node] = self.findUPar(self.parent[node])
        return self.parent[node]
    
    def union_by_rank(self , u , v):
        upu = self.findUPar(u)
        upv = self.findUPar(v)

        if upv==upu:
            return False
        if self.rank[upu] < self.rank[upv]:
            self.parent[upu]=upv
        elif (self.rank[upv]<self.rank[upu]):
            self.parent[upv]=upu
        else:
            self.parent[upu]=upv
            self.rank[upv]+=1

    def union_by_size(self , u , v):
        upu = self.findUPar(u)
        upv = self.findUPar(v)

        if upu==upv:
            return False

        if self.size[u]<self.size[v]:
            self.parent[u]=v
            self.size[v]+=self.size[u]
        else:
            self.parent[v]=u
            self.size[u]+=self.size[v]
        return True

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        ds =DisjointSet(n)
        for u , v in edges:
            ds.union_by_rank(u,v)  
        return ds.findUPar(source)==ds.findUPar(destination)