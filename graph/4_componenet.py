"""

Given an undirected graph with V vertices. We say two vertices u and v belong to a
single province if there is a path from u to v or v to u. Your task is to find the 
number of provinces.

Note: A province is a group of directly or indirectly connected cities and no other 
cities outside of the group.


"""



class Solution:
    
    def convert_adj_matrix_to_list(self,adj_matrix):
        V = len(adj_matrix)
        adj_list = [[] for _ in range(V)]
        
        for i in range(V):
            for j in range(V):
                if adj_matrix[i][j] == 1 and i != j:
                    adj_list[i].append(j)
        
        return adj_list
    
    
    def dfs(self,start,V,adj,vis):
        stack=list()
        stack.append(start)
        vis[start]=True
        # ans=[]
        
        while(len(stack)!=0):
            top=stack.pop()
            # ans.append(top)
            for i in adj[top]:
                if vis[i]==False:
                    stack.append(i)
                    vis[i]=True
        return
        
    
    
    def numProvinces(self, adj, V):
        n=V
        vis=[False]*n
        count=0
        
        adj_lst = self.convert_adj_matrix_to_list(adj)
        
        for i in range(0,n,1):
            if(vis[i]==False):
                self.dfs(i,V,adj_lst,vis)
                count+=1
        return count
 