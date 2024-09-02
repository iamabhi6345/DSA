class DisjointSet:
    def __init__(self, n):
        self.rank = [0] * (n + 1)
        self.parent = list(range(n + 1))
        self.size = [1] * (n + 1)
    
    def find(self, node):
        if node != self.parent[node]:
            self.parent[node] = self.find(self.parent[node])  # Path compression
        return self.parent[node]
    
    def union_by_rank(self, u, v):
        ulp_u = self.find(u)
        ulp_v = self.find(v)
        if ulp_u != ulp_v:
            if self.rank[ulp_u] < self.rank[ulp_v]:
                self.parent[ulp_u] = ulp_v
            elif self.rank[ulp_u] > self.rank[ulp_v]:
                self.parent[ulp_v] = ulp_u
            else:
                self.parent[ulp_v] = ulp_u
                self.rank[ulp_u] += 1
    
    def union_by_size(self, u, v):
        ulp_u = self.find(u)
        ulp_v = self.find(v)
        if ulp_u != ulp_v:
            if self.size[ulp_u] < self.size[ulp_v]:
                self.parent[ulp_u] = ulp_v
                self.size[ulp_v] += self.size[ulp_u]
            else:
                self.parent[ulp_v] = ulp_u
                self.size[ulp_u] += self.size[ulp_v]

class Solution:
    def __init__(self):
        self.directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    
    def is_valid(self, r, c, n, m):
        return 0 <= r < n and 0 <= c < m
    
    def num_of_islands(self, n, m, operators):
        ds = DisjointSet(n * m)
        vis = [[0] * m for _ in range(n)]
        cnt = 0
        ans = []
        
        for row, col in operators:
            if vis[row][col] == 1:
                ans.append(cnt)
                continue
            vis[row][col] = 1
            cnt += 1
            node_no = row * m + col
            for dr, dc in self.directions:
                adjr, adjc = row + dr, col + dc
                if self.is_valid(adjr, adjc, n, m) and vis[adjr][adjc] == 1:
                    adj_node_no = adjr * m + adjc
                    if ds.find(node_no) != ds.find(adj_node_no):
                        cnt -= 1
                        ds.union_by_size(node_no, adj_node_no)
            ans.append(cnt)
        
        return ans

# Example usage
if __name__ == "__main__":
    n = 4
    m = 5
    operators = [
        [0, 0], [0, 0], [1, 1], [1, 0], [0, 1],
        [0, 3], [1, 3], [0, 4], [3, 2], [2, 2],
        [1, 2], [0, 2]
    ]
    
    obj = Solution()
    ans = obj.num_of_islands(n, m, operators)
    print(" ".join(map(str, ans)))
