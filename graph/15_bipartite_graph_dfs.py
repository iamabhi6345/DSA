class Solution:
    def __dfs(self, s, adj,color):
        
        stack=[]
        stack.append((s,0))
        
        while stack:
            r,clr = stack.pop()
            for i in adj[r]:
                if color[i]==-1:
                    stack.append((i,1-clr))
                    color[i]=1-clr
                elif (color[i]==clr):
                    return False
            
        return True
        
    def isBipartite(self, V, adj):
        #code here
        nr=len(adj)
        color=[-1]*V

        for i in range(V):
            if color[i]==-1:
                if self.__dfs(i,adj,color)==False:
                    return False
        return True 