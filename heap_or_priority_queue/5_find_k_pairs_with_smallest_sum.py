import heapq
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        ans = []
        pq = []
        
        for i in range(min(k , len(nums1))):
            sm = nums1[i]+nums2[0]
            heapq.heappush(pq , (sm , i , 0) )
        
        while pq and len(ans)<k:
            sm , i , j = heapq.heappop(pq)
            ans.append((nums1[i] , nums2[j]))

            if j+1 < len(nums2):
                sm = nums1[i] + nums2[j+1]
                heapq.heappush(pq , (sm , i , j+1))

        return ans
