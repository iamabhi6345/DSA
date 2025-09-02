from collections import deque

class Solution:
    # Function to return Breadth First Search Traversal of given graph.
    
    
    def bfs(self, adj):
        # code here
        node = len(adj)
        vis=[0]*node
        q=deque()
        q.append(0)
        vis[0]=1
        
        bfs=[]
        
        while(len(q)!=0):
            tmp_node = q.popleft()
            bfs.append(tmp_node)
            
            for x in adj[tmp_node]:
                if vis[x]==0:
                    q.append(x)
                    vis[x]=1
        
        return bfs
            
        
        
                
