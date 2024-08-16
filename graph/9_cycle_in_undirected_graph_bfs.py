


from typing import List
from collections import deque

class Solution:
    def detect(self ,start ,  adj , vis):
        dq=deque()
        dq.append((start,-1))
        vis[start]=True
        
        while dq:
            c , p = dq.popleft()
            for i in adj[c]:
                if not vis[i]:
                    dq.append((i,c))
                    vis[i]=True
                
                elif (i!=p):
                    return True
        
        return False
        
        
    #Function to detect cycle in an undirected graph.
    def isCycle(self, V: int, adj: List[List[int]]) -> bool:
        #Code here
        vis=[False]*V

        for i in range(V):
            if not vis[i]:
                if(self.detect(i,adj,vis)):
                    return True
        return False 
