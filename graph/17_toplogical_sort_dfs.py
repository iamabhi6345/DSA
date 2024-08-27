class Solution:
    def dfs ( self , start , adj, vis , st):
            vis[start]=True
            for i in adj[start]:
                if vis[i]==False:
                    self.dfs(i , adj , vis , st)
            st.append(start)



    def topoSort(self, V, adj):
        # Code here
        stack=[]
        vis = [False]*V
        for i in range(V):
            if vis[i]==False:
                self.dfs(i , adj , vis , stack)
        
        ans =[]
        while (stack):
            top = stack.pop()
            ans.append(top)
        
        return ans
            
