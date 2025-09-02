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
            

# =================================================================================================================================
"""

✅ Time Complexity

Each vertex (node) is:
Added to queue once
Removed from queue once
Marked visited once
→ O(V)

Each edge is checked once in the adjacency list.
→ O(E)

📌 Total = O(V + E) (this is optimal BFS complexity).

✅ Space Complexity

vis array → O(V)
bfs result list → O(V)
q (queue) → can hold up to O(V) elements in worst case
Adjacency list storage (input adj) → O(V + E)

📌 Auxiliary space = O(V)
📌 Overall space = O(V + E)

"""
        
                
