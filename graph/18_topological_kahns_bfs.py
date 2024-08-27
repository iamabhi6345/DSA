# indegree concept

from collections import deque

class Solution:
    
    #Function to return list containing vertices in Topological order.
    def topoSort(self, v, adj):
        # Code here
        q = deque()

        indegree=[0]*v
        for i in range(v):
            for i in adj[i]:
                indegree[i]+=1

        for i in range(v):
            if indegree[i]==0:
                q.append(i)

        ans =[]

        while(q):
            top = q.popleft()
            ans.append(top)
            for i in adj[top]:
                indegree[i]-=1
                if indegree[i]==0:
                    q.append(i)

        return ans


def check(graph, N, res):
    if N != len(res):
        return False
    
    map = [0] * N
    for i in range(N):
        map[res[i]] = i

    for i in range(N):
        for v in graph[i]:
            if map[i] > map[v]:
                return False

    return True

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        e, N = list(map(int, input().strip().split()))
        adj = [[] for i in range(N)]
        
        for i in range(e):
            u, v = map(int, input().split())
            adj[u].append(v)
        
        ob = Solution()  # Corrected instance creation
        res = ob.topoSort(N, adj)  # Corrected method call
        print(res)
        
        if check(adj, N, res):
            print(1)
        else:
            print(0)
