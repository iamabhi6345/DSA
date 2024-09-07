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
    

    def removeStones(self, stones: List[List[int]]) -> int:
        mr=0
        mc=0
        for x in stones:
            mr = max(mr , x[0])
            mc = max(mc , x[1])
        
        ds = DisjointSet(mr+mc+2)


        for x in stones:
            row=x[0]
            col=x[1]+mr+1
            ds.union_by_size(row , col)
         
        
        comp=0
        for i in range(mc+mr+2):
            if ds.size[i]>1 and ds.parent[i]==i:
                comp+=1
        n= len(stones)
        return n-comp
   


# Example usage
if __name__ == "__main__":
    n = 6
    stones = [
        [0, 0], [0, 2],
        [1, 3], [3, 1],
        [3, 2], [4, 3]
    ]
    
    obj = Solution()
    ans = obj.removeStones(stones)
    print(f"The maximum number of stones we can remove is: {ans}")
