import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pq = []
        for i in nums:
            heapq.heappush(pq , -i)
        ans=0
        for i in range(k):
            ans = heapq.heappop(pq)
        return -ans

"""  
above tc will go up to n log n
below it will be n log k
k<n
so below is better
log k because heap sioze will always will be less than equal to k
"""

# ????? optimizxation
import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pq = []
        
        for i in nums:
            heapq.heappush(pq , i)
            if len(pq)>k:
                heapq.heappop(pq)

        return heapq.heappop(pq)