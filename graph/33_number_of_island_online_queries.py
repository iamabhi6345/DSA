#User function Template for python3

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
        self.directions = [(-1,0),(0,1),(1,0),(0,-1)]
        
    def numOfIslands(self, nr: int, nc : int, operators : List[List[int]]) -> List[int]:
        # code here
        ds = DisjointSet(nr*nc)
        arr = [ [0]*nc for _ in range(nr)]
        count=0
        ans=[]
        for i , j in operators:
            if arr[i][j]==1:
                ans.append(count)
                continue
            count+=1
            arr[i][j]=1
 
            node = i*nc + j
            for di , dj in self.directions:
                ni = i+di
                nj = j+dj
                if(0<=ni<nr) and (0<=nj<nc) and (arr[ni][nj]==1):
                    adj_node = ni*nc + nj
                    tmp_par=ds.find(adj_node)
                    if ds.union_by_size(node,adj_node):
                    # if ds.union_by_rank(node,adj_node):
                        count-=1
            ans.append(count)
        return ans


if __name__ == "__main__":
    n = 4
    m = 5
    operators = [
        [0, 0], [0, 0], [1, 1], [1, 0], [0, 1],
        [0, 3], [1, 3], [0, 4], [3, 2], [2, 2],
        [1, 2], [0, 2]
    ]

    obj = Solution()
    ans = obj.numOfIslands(n, m, operators)
    print(" ".join(map(str, ans)))


# Output: 1 1 2 1 1 2 2 2 3 3 1 1