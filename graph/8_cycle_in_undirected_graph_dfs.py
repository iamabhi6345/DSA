from typing import List

class Solution:
    
    def __detect(self, start, adj, vis):
        stack = []
        stack.append((start, -1))  # Use append instead of push
        vis[start] = True
        
        while stack:
            c, p = stack.pop()
            
            for i in adj[c]:
                if not vis[i]:
                    stack.append((i, c))
                    vis[i] = True
                elif i != p:
                    return True
                 
        return False
        
    # Function to detect cycle in an undirected graph.
    def isCycle(self, V: int, adj: List[List[int]]) -> bool:
        vis = [False] * V
        
        for i in range(V):
            if not vis[i]:
                if self.__detect(i, adj, vis):
                    return True
        return False
