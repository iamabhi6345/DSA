"""   
A bipartite graph is a graph in which the vertices can be divided into two disjoint sets,
such that no two vertices within the same set are adjacent. In other words, it is a graph
in which every edge connects a vertex of one set to a vertex of the other set.
"""



from collections import deque
class Solution:
    def __bfs(self, s, color,adj):
        nr=len(adj)
        dq=deque()
        dq.append((s))
        color[s]=0

        while dq:
            c=dq.popleft()
            for i in adj[c]:
                if color[i]==-1:
                    dq.append((i))
                    color[i]=1-color[c]
                elif color[i]==color[c]:
                    return False
        return True  
  
    def isBipartite(self, V, adj):
    #code here
        nr=len(adj)

        color=[-1]*nr

        for i in range(V):
            if (color[i]==-1):
                if self.__bfs(i,color,adj)==False:
                    return False

        return True           
		        
	