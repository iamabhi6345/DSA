class Solution:

    def dfsOfGraph(self, V, adj):

        ans=list()
        stack=[]
        stack.append(0)
        visited=[False]*V
        visited[0]=True
        
        while(len(stack)!=0):
            top=stack.pop()
            ans.append(top)
            for i in adj[top]:
                if visited[i]==False:
                    stack.append(i)
                    visited[i]=True
        return ans