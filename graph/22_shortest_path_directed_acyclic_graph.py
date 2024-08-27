"""   

Given a Directed Acyclic Graph of N vertices from 0 to N-1 and a 2D Integer array(or vector) edges[ ][ ] of length M, where there is a directed edge from edge[i][0] to edge[i][1] with a distance of edge[i][2] for all i.

Find the shortest path from src(0) vertex to all the vertices and if it is impossible to reach any vertex, then return -1 for that vertex.

Example1:

Input:
N = 4, M = 2
edge = [[0,1,2],[0,2,1]]
Output:
0 2 1 -1
Explanation:
Shortest path from 0 to 1 is 0->1 with edge weight 2. 
Shortest path from 0 to 2 is 0->2 with edge weight 1.
There is no way we can reach 3, so it's -1 for 3.
Example2:

Input:
N = 6, M = 7
edge = [[0,1,2],[0,4,1],[4,5,4],[4,2,2],[1,2,3],[2,3,6],[5,3,1]]
Output:
0 2 3 6 1 5
Explanation:
Shortest path from 0 to 1 is 0->1 with edge weight 2. 
Shortest path from 0 to 2 is 0->4->2 with edge weight 1+2=3.
Shortest path from 0 to 3 is 0->4->5->3 with edge weight 1+4+1=6.
Shortest path from 0 to 4 is 0->4 with edge weight 1.
Shortest path from 0 to 5 is 0->4->5 with edge weight 1+4=5.
Your Task:

You don't need to print or input anything. Complete the function shortest path() which takes an integer N as number of vertices, an integer M as number of edges and a 2D Integer array(or vector) edges as the input parameters and returns an integer array(or vector), denoting the list of distance from src to all nodes.

Expected Time Complexity: O(N+M), where N is the number of nodes and M is edges
Expected Space Complexity: O(N)


Constraint:
1 <= N <= 100
1 <= M <= min((N*(N-1))/2,4000)
0 <= edgei,0,edgei,1 < n
0 <= edgei,2 <=105


Time Complexity: O(N+M) {for the topological sort} + O(N+M) {for relaxation of 
vertices, each node and its adjacent nodes get traversed} ~ O(N+M).

Where N= number of vertices and M= number of edges.

Space Complexity:  O( N) {for the stack storing the topological sort} + O(N) 
{for storing the shortest distance for each node} + O(N) {for the visited array} 
+ O( N+2M) {for the adjacency list} ~ O(N+M) .


"""





#User function Template for python3

from typing import List

class Solution:
    
    def __dfs(self , start , vis , stack , adj):
        vis[start]=True
        for i in adj[start]:
            if vis[i[0]]==False:
                self.__dfs(i[0] , vis , stack , adj)
        stack.append(start)
        
        
    def shortestPath(self, n : int, m : int, edges : List[List[int]]) -> List[int]:
        adj =[[] for _ in range(n)]
        
        for i in range(m):
            adj[edges[i][0]].append([   edges[i][1]  , edges[i][2] ] )
        
        stack=[]
        vis=[False]*n
        for i in range(n):
            if vis[i]==False:
                self.__dfs(i , vis , stack , adj)
        
        
        dist = [1e9]*n
        dist[0]=0
        
        while(stack):
            top= stack.pop()
            for i in adj[top]:
                tmp = dist[top] + i[1]
                if tmp < dist[i[0]]:
                    dist[i[0]] = tmp
        
        for i in range(n):
            if dist[i]==1e9:
                dist[i]=-1
        return dist

