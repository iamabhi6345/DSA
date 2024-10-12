class Solution:
    def solve(self, i, nums, last, dp):
        if i < 0:
            return 0

        if i == 0:
            print(i , last )
            if last == False:
                
                return nums[0]
            else:
                return 0

        if dp[i] != -1:
            return dp[i]

        if i == len(nums) - 1:
            
            take = nums[i] + self.solve(i - 2, nums, True, dp)
            nottake = self.solve(i - 1, nums, False, dp)
            dp[i] = max(take, nottake)
            return dp[i]

        nottake = self.solve(i - 1, nums, last, dp)
        take = nums[i] + self.solve(i - 2, nums, last, dp)

        dp[i] = max(take, nottake)
        return dp[i]

    def rob(self, nums):
        if len(nums) == 1:
            return nums[0]
        
        dp = [-1] * len(nums)
        return self.solve(len(nums) - 1, nums, False, dp)


def main():
  
    nums=[200,3,140,20,10]

    solution = Solution()

    result = solution.rob(nums)
    print("Maximum money that can be robbed:", result)


if __name__ == "__main__":
    main()
