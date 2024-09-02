from typing import List
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
            return False
        if self.rank[ulp_u] < self.rank[ulp_v]:
            self.parent[ulp_u] = ulp_v
        elif self.rank[ulp_v] < self.rank[ulp_u]:
            self.parent[ulp_v] = ulp_u
        else:
            self.parent[ulp_v] = ulp_u
            self.rank[ulp_u] += 1
        return True
        
    def union_by_size(self, u, v):
        ulp_u = self.find(u)
        ulp_v = self.find(v)
        if ulp_u == ulp_v:
            return False
        if self.size[ulp_u] < self.size[ulp_v]:
            self.parent[ulp_u] = ulp_v
            self.size[ulp_v] += self.size[ulp_u]
        else:
            self.parent[ulp_v] = ulp_u
            self.size[ulp_u] += self.size[ulp_v]
        return True


class Solution:
    def __init__(self):
        self.directions= [(-1,0),(0,1),(1,0),(0,-1)]
    def MaxConnection(self, grid : List[List[int]]) -> int:
        # code here
        n = len(grid)
        ds = DisjointSet(n*n)
        for i in range(n):
            for j in range(n):
                if grid[i][j]==1:
                    node = i*n + j
                    for di ,dj in self.directions:
                        ni=i+di
                        nj=j+dj
                        if (0<=ni<n) and (0<=nj<n) and grid[ni][nj]==1:
                            adj_node = ni*n + nj
                            ds.union_by_size(node,adj_node)
        
        
        maxi=-1
        for i in range(n):
            for j in range(n):
                if grid[i][j]==0:
                    node = i*n + j
                    tmp = set()
                    for di , dj in self.directions:
                        ni = i+ di
                        nj = j+ dj
                        if (0<=ni<n) and (0<=nj<n) and (grid[ni][nj]==1):
                            adj_node = ni*n + nj
                            par = ds.find(adj_node)
                            tmp.add(par)
                    sum_tmp=1
                    for x in tmp:
                        sum_tmp+=ds.size[x]
                    maxi = max(sum_tmp , maxi)
        
        # for node in range(n*n):
        #     maxi = max(maxi , ds.size[ds.find(node)])
        if maxi==-1:
            maxi=n*n
        return maxi


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
