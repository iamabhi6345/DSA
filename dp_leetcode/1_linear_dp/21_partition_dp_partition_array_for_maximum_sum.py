"""   
Given an integer array arr, partition the array into (contiguous) subarrays of length at most k. After partitioning, each subarray has their values changed to become the maximum value of that subarray.

Return the largest sum of the given array after partitioning. Test cases are generated so that the answer fits in a 32-bit integer.

 

Example 1:

Input: arr = [1,15,7,9,2,5,10], k = 3
Output: 84
Explanation: arr becomes [15,15,15,9,10,10,10]
Example 2:

Input: arr = [1,4,1,5,7,3,6,1,9,9,3], k = 4
Output: 83
Example 3:

Input: arr = [1], k = 1
Output: 1
 

Constraints:

1 <= arr.length <= 500
0 <= arr[i] <= 109
1 <= k <= arr.length

"""

class Solution:

    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n= len(arr)
        dp=[0]*(n+1)

        for i in range(n-1,-1,-1):
            length =0
            maxi = int(-1e8)
            ans = int(-1e8)
            for j in range(i , min(i+k , n)):
                length+=1
                maxi = max(maxi , arr[j])
                cost = length*maxi + dp[j+1]
                ans = max(ans,cost)
            dp[i] = ans
        return dp[0]




class Solution:
    def solve(self , ind , dp , arr , k ):
        if ind ==len(arr):
            return 0
        if dp[ind]!=-1:
            return dp[ind]
        length =0 
        maxi=int(-1e8)
        ans=int(-1e8)

        for j in range(ind , min(ind+k  , len(arr))):
            length+=1
            maxi = max(maxi , arr[j])
            cost = length*maxi + self.solve(j+1 , dp , arr , k)
            ans = max(ans , cost)

        dp[ind] = ans 
        return dp[ind]

    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        dp= [-1]*(len(arr))
        return self.solve(0,dp,arr , k)
