#User function Template for python3
from typing import List

class Solution:
    
    def __dfs(self,vis,path,adj,node):
        
        vis[node]=True
        path[node]=True
        
        for i in adj[node]:
            if vis[i]==False:
                if self.__dfs(vis,path,adj,i):
                    return True
            elif path[i]==True:
                return True
                
        
        path[node]=False
        return False
        

    #Function to detect cycle in a directed graph.
    def isCyclic(self, V : int , adj : List[List[int]]) -> bool :
        
        vis=[False]*V
        path=[False]*V
        for i in range(V):
            if vis[i]==False:
                if self.__dfs(vis,path,adj,i):
                    return True
        
        return False