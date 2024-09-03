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
    def maxRemove(self, stones, n):
        maxRow = 0
        maxCol = 0
        
        # Find the maximum row and column indices
        for stone in stones:
            maxRow = max(maxRow, stone[0])
            maxCol = max(maxCol, stone[1])
        
        # Create DisjointSet with size large enough to include all rows and columns
        ds = DisjointSet(maxRow + maxCol + 2)
        
        # Union operations for rows and columns
        stoneNodes = {}
        for stone in stones:
            nodeRow = stone[0]
            nodeCol = stone[1] + maxRow + 1
            ds.union_by_size(nodeRow, nodeCol)
            stoneNodes[nodeRow] = 1
            stoneNodes[nodeCol] = 1
        
        # Count the number of disjoint sets
        cnt = 0
        for node in stoneNodes:
            if ds.find(node) == node:
                cnt += 1
        
        return n - cnt

# Example usage
if __name__ == "__main__":
    n = 6
    stones = [
        [0, 0], [0, 2],
        [1, 3], [3, 1],
        [3, 2], [4, 3]
    ]
    
    obj = Solution()
    ans = obj.maxRemove(stones, n)
    print(f"The maximum number of stones we can remove is: {ans}")
