#User function Template for python3
from typing import List
from collections import deque

class Solution:

    def topo(self, v, adj):
        # Code here
        q = deque()

        indegree=[0]*v
        for i in range(v):
            for i in adj[i]:
                indegree[i]+=1

        for i in range(v):
            if indegree[i]==0:
                q.append(i)

        count=0

        while(q):
            top = q.popleft()
            count+=1
            for i in adj[top]:
                indegree[i]-=1
                if indegree[i]==0:
                    q.append(i)

        return count!=v
            
    
    #Function to detect cycle in a directed graph.
    def isCyclic(self, V : int , adj : List[List[int]]) -> bool :
        # code here
        return self.topo(V,adj)
