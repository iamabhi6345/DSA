""" 
834. Sum of Distances in Tree
Solved
Hard
Topics
Companies
There is an undirected connected tree with n nodes labeled from 0 to n - 1 and n - 1 edges.

You are given the integer n and the array edges where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the tree.

Return an array answer of length n where answer[i] is the sum of the distances between the ith node in the tree and all other nodes.

 

Example 1:


Input: n = 6, edges = [[0,1],[0,2],[2,3],[2,4],[2,5]]
Output: [8,12,6,10,10,10]
Explanation: The tree is shown above.
We can see that dist(0,1) + dist(0,2) + dist(0,3) + dist(0,4) + dist(0,5)
equals 1 + 1 + 2 + 2 + 2 = 8.
Hence, answer[0] = 8, and so on.
Example 2:


Input: n = 1, edges = []
Output: [0]
Example 3:


Input: n = 2, edges = [[1,0]]
Output: [1,1]
 

"""

class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        # Arrays to store the size of each subtree and the sum of distances
        subtree_size = [1] * n
        result = [0] * n
        
        # First DFS to calculate subtree sizes and initial sum of distances 
        # from node 0
        def dfs1(node, parent):
            for neighbor in adj[node]:
                if neighbor != parent:
                    dfs1(neighbor, node)
                    subtree_size[node] += subtree_size[neighbor]
                    result[0] += result[neighbor] + subtree_size[neighbor]
        
        # Second DFS to propagate the result from node 0 to all other nodes
        def dfs2(node, parent):
            for neighbor in adj[node]:
                if neighbor != parent:
                    result[neighbor] = result[node] + (n - subtree_size[neighbor]) - subtree_size[neighbor]
                    dfs2(neighbor, node)
        
        # Start the first DFS from node 0
        dfs1(0, -1)
        
        # Start the second DFS to propagate the result to all other nodes
        dfs2(0, -1)
        
        return result



# ?????????????? brute force   --(will give TLE) 

from collections import deque
class Solution:
    def bfs(self , start , adj , n):
        visited= [False]*n
        q = deque()
        q.append((start , 0))
        visited[start]=True
        ans=0
        while q:
            top , dist = q.popleft()
            ans+=dist
            for i in adj[top]:
                if visited[i]==False:
                    q.append((i,dist+1))
                    visited[i]=True
        return ans


    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        adj = [ [] for _ in range(n)]
        for a , b in edges:
            adj[a].append(b)
            adj[b].append(a)

        ans=[0]*n
        for i in range(n):
            ans[i]=self.bfs(i,adj,n)
        return ans
        