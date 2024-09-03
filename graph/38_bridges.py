from collections import defaultdict

class Solution:
    def __init__(self):
        self.timer = 1

    def dfs(self, node, parent, vis, adj, tin, low, bridges):
        vis[node] = True
        tin[node] = low[node] = self.timer
        self.timer += 1
        
        for it in adj[node]:
            if it == parent:
                continue
            if not vis[it]:
                self.dfs(it, node, vis, adj, tin, low, bridges)
                low[node] = min(low[node], low[it])
                # node --- it
                if low[it] > tin[node]:
                    bridges.append([it, node])
            else:
                low[node] = min(low[node], tin[it])

    def criticalConnections(self, n, connections):
        adj = defaultdict(list)
        for u, v in connections:
            adj[u].append(v)
            adj[v].append(u)
        
        vis = [False] * n
        tin = [-1] * n
        low = [-1] * n
        bridges = []
        
        # Assuming the graph is connected, we start DFS from node 0
        self.dfs(0, -1, vis, adj, tin, low, bridges)
        
        return bridges


if __name__ == "__main__":
    n = 4
    connections = [
        [0, 1], [1, 2],
        [2, 0], [1, 3]
    ]

    obj = Solution()
    bridges = obj.criticalConnections(n, connections)
    for bridge in bridges:
        print(f"[{bridge[0]}, {bridge[1]}]", end=" ")
    print()
