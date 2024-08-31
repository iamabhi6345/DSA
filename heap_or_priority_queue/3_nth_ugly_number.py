import heapq
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        pq = []
        seen = set()
        heapq.heappush(pq , 1)
        seen.add(1)
        ans=0
        for i in range(n):
            ans = heapq.heappop(pq)
            for i in [2,3,5]:
                ele = ans*i
                if ele not in seen:
                    heapq.heappush(pq , ele)
                    seen.add(ele)
        return ans
    


