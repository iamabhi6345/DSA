class Solution:
    
    #Function to return a list containing the DFS traversal of the graph.
    def dfs(self, adj):
        # code here
        node = len(adj)
        vis=[0]*node
        ans=[]
        
        def f(ind):
            vis[ind]=1
            ans.append(ind)
            
            for x in adj[ind]:
                if vis[x]==0:
                    f(x)
        
        f(0)
        return ans



"""
✅ Complexity

Time Complexity:
Each vertex visited once → O(V)
Each edge explored once → O(E)
Total = O(V + E)` (optimal for DFS).

Space Complexity:
vis array → O(V)
Recursion stack in worst case (skewed graph) → O(V)
ans → O(V)

Total = O(V)`
"""
