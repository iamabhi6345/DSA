class Solution:
    
    # Function to perform DFS and fill the stack with vertices in the order of their finishing times
    def DFS1(self, v, visited, stack, adj):
        visited[v] = True
        for i in adj[v]:
            if not visited[i]:
                self.DFS1(i, visited, stack, adj)
        stack.append(v)

    # Function to perform DFS on the transposed graph
    def DFS2(self, v, visited, transpose):
        visited[v] = True
        for i in transpose[v]:
            if not visited[i]:
                self.DFS2(i, visited, transpose)

    # Function to transpose the graph
    def getTranspose(self, V, adj):
        transpose = [[] for _ in range(V)]
        for v in range(V):
            for i in adj[v]:
                transpose[i].append(v)
        return transpose

    # Function to find the number of strongly connected components in the graph.
    def kosaraju(self, V, adj):
        stack = []
        visited = [False] * V
        
        # Step 1: Perform DFS to store vertices in stack according to their finishing times
        for i in range(V):
            if not visited[i]:
                self.DFS1(i, visited, stack, adj)
        
        # Step 2: Get the transpose of the graph
        transpose = self.getTranspose(V, adj)
        
        # Step 3: Perform DFS on the transposed graph in the order of vertices in stack
        visited = [False] * V
        count = 0
        while stack:
            v = stack.pop()
            if not visited[v]:
                self.DFS2(v, visited, transpose)
                count += 1
        
        return count

# Example usage:
if __name__ == "__main__":
    V = 7
    adj = [[] for _ in range(V)]
    adj[0].append(1)
    adj[1].append(2)
    adj[1].append(3)
    adj[3].append(4)
    adj[4].append(0)
    adj[4].append(5)
    adj[4].append(6)
    adj[5].append(6)
    adj[6].append(5)

    solution = Solution()
    print("Number of SCCs is:", solution.kosaraju(V, adj))
