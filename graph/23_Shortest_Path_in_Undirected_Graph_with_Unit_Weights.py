"""   

You are given an Undirected Graph having unit weight of the edges, find the shortest path from src to all the vertex and if it is unreachable to reach any vertex, then return -1 for that vertex.

Examples :

Input:
n = 9, m = 10
edges=[[0,1],[0,3],[3,4],[4,5],[5,6],[1,2],[2,6],[6,7],[7,8],[6,8]] 
src=0
Output:
0 1 2 1 2 3 3 4 4

Input:
n = 4, m = 2
edges=[[1,3],[3,0]] 
src=3
Output:
1 1 -1 0

Constraint:
1<=n,m<=104
0<=edges[i][j]<=n-1

Expected Time Complexity: O(N + E), where N is the number of nodes and E is the edges
Expected Space Complexity: O(N)

"""


#User function Template for python3
from collections import deque
class Solution:
    def shortestPath(self, edges, n, m, src):
        # code here
        adj = [[] for _ in range(n)]
        for i in edges:
            adj[i[0]].append(i[1])
            adj[i[1]].append(i[0])
        
        distance=[1e9]*n
        distance[src]=0

        q = deque()
        q.append((src,0))
        
        while(q):
            node , dist = q.popleft()
            
            for i in adj[node]:
                if dist + 1 < distance[i]:
                    distance[i] = 1 + dist
                    q.append((i , dist+1))
        
        for i in range(n):
            if distance[i]==1e9:
                distance[i]=-1
        return distance
                
