

import heapq
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        pq = []
        seen = set()
        heapq.heappush(pq , (matrix[0][0] , 0 , 0)  )
        seen.add((0,0))
        ans = 0
        r = len(matrix)
        c = len(matrix[0])


        for _ in range(k):
            ans , i , j = heapq.heappop(pq)
           
            if i+1<r and (i+1,j) not in seen:
                heapq.heappush(pq , (matrix[i+1][j] , i+1 , j))
                seen.add((i+1,j))
            
            if j+1<c and (i , j+1) not in seen:
                heapq.heappush(pq , (matrix[i][j+1] , i , j+1))
                seen.add((i,j+1))
        return ans