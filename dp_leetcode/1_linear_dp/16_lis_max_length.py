"""  
Given an integer array nums, return the length of the longest strictly increasing 
subsequence
.

 

Example 1:

Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
Example 2:

Input: nums = [0,1,0,3,2,3]
Output: 4
Example 3:

Input: nums = [7,7,7,7,7,7,7]
Output: 1
 

lis = longest increasing subsequence
"""
#  binary search --O(n*log n)

import bisect
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp=[nums[0]]
        ans =1
        for i in range(n):
            if nums[i]>dp[-1]:
                ans+=1
                dp.append(nums[i])
            else:
                ind = bisect.bisect_left(dp , nums[i])
                dp[ind]=nums[i]
        return ans



# tabulation  -- O(n^2)

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp=[1]*n
        ans =1
        for i in range(1,n):
            for j in range(i):
                if nums[i]>nums[j] and 1+ dp[j]>dp[i]:
                    dp[i]=1+dp[j]
            ans = max(ans , dp[i])
        return ans



# memoization---> it can give TLE

class Solution:
    def f ( self, ind , prev , dp , arr):
        if ind==len(arr):
            return 0
        if dp[ind][prev+1]!=-1:
            return dp[ind][prev+1]
        take =0
        if prev==-1 or arr[ind]>arr[prev]:
            take = 1 + self.f(ind+1 , ind, dp , arr)
        nottake = self.f(ind+1,prev , dp , arr)
        dp[ind][prev+1]=max(take , nottake)
        return dp[ind][prev+1]

    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[-1]*(n+1) for _ in range(n)]
        return self.f(0,-1,dp,nums)
            

