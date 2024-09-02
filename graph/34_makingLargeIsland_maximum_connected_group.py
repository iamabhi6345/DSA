class DisjointSet:
    def __init__(self, n):
        self.rank = [0] * (n + 1)
        self.parent = list(range(n + 1))
        self.size = [1] * (n + 1)
    
    def find(self, node):
        if node != self.parent[node]:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]
    
    def union_by_rank(self, u, v):
        ulp_u = self.find(u)
        ulp_v = self.find(v)
        if ulp_u == ulp_v:
            return
        if self.rank[ulp_u] < self.rank[ulp_v]:
            self.parent[ulp_u] = ulp_v
        elif self.rank[ulp_v] < self.rank[ulp_u]:
            self.parent[ulp_v] = ulp_u
        else:
            self.parent[ulp_v] = ulp_u
            self.rank[ulp_u] += 1
    
    def union_by_size(self, u, v):
        ulp_u = self.find(u)
        ulp_v = self.find(v)
        if ulp_u == ulp_v:
            return
        if self.size[ulp_u] < self.size[ulp_v]:
            self.parent[ulp_u] = ulp_v
            self.size[ulp_v] += self.size[ulp_u]
        else:
            self.parent[ulp_v] = ulp_u
            self.size[ulp_u] += self.size[ulp_v]

class Solution:
    def __init__(self):
        self.directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    
    def is_valid(self, newr, newc, n):
        return 0 <= newr < n and 0 <= newc < n
    
    def MaxConnection(self, grid):
        n = len(grid)
        ds = DisjointSet(n * n)
        
        # Step 1
        for row in range(n):
            for col in range(n):
                if grid[row][col] == 0:
                    continue
                node_no = row * n + col
                for dr, dc in self.directions:
                    newr, newc = row + dr, col + dc
                    if self.is_valid(newr, newc, n) and grid[newr][newc] == 1:
                        adj_node_no = newr * n + newc
                        ds.union_by_size(node_no, adj_node_no)
        
        # Step 2
        mx = 0
        for row in range(n):
            for col in range(n):
                if grid[row][col] == 1:
                    continue
                components = set()
                for dr, dc in self.directions:
                    newr, newc = row + dr, col + dc
                    if self.is_valid(newr, newc, n):
                        if grid[newr][newc] == 1:
                            components.add(ds.find(newr * n + newc))
                
                size_total = sum(ds.size[comp] for comp in components)
                mx = max(mx, size_total + 1)
        
        for cell_no in range(n * n):
            mx = max(mx, ds.size[ds.find(cell_no)])
        
        return mx

# Example usage
if __name__ == "__main__":
    grid = [
        [1, 1, 0, 1, 1, 0], [1, 1, 0, 1, 1, 0],
        [1, 1, 0, 1, 1, 0], [0, 0, 1, 0, 0, 0],
        [0, 0, 1, 1, 1, 0], [0, 0, 1, 1, 1, 0]
    ]
    
    obj = Solution()
    ans = obj.MaxConnection(grid)
    print(f"The largest group of connected 1s is of size: {ans}")
