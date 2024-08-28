"""  
Given an integer array nums, return true if you can partition the array into two subsets such that the sum of the elements in both subsets is equal or false otherwise.

 

Example 1:

Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].
Example 2:

Input: nums = [1,2,3,5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets.
 

Constraints:

1 <= nums.length <= 200
1 <= nums[i] <= 100

"""



class Solution:
    def solve(self , ind , tot , nums , dp):
        if tot ==0:
            return True
        if ind ==0:
            return tot == nums[0]
        
        if dp[ind][tot]!=-1:
            return dp[ind][tot]
        
        take = False
        if nums[ind] <= tot:
            take = self.solve(ind-1,tot-nums[ind],nums,dp)
        nottake=self.solve(ind-1,tot,nums,dp)
        dp[ind][tot]=take|nottake
        return dp[ind][tot]


    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total &1:
            return False
        k = total>>1
        n=len(nums)
        dp = [ [-1]*(k+1) for _ in range(n)]
        return self.solve(n-1 , k,nums, dp)
        