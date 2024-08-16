
# memoization
class Solution:
    def solve(self,n, arr):
        if n<=1:
            return n

        if arr[n]!=-1:
            return arr[n]
        arr[n]=self.solve(n-1,arr) + self.solve(n-2,arr)
        return arr[n]


    def fib(self, n: int) -> int:
        arr=[-1]*(n+1)
        return self.solve(n,arr)


# tabulation

class Solution:
    def fib(self, n: int) -> int:
        if (n<=1):
            return n
        dp=[-1]*(n+1)
        dp[0]=0
        dp[1]=1
        for i in range(2,n+1):
            dp[i]=dp[i-1]+dp[i-2]
        return dp[n]
    

# space optimization

class Solution:
    def fib(self, n: int) -> int:
        if (n<=1):
            return n
        prev2=0
        prev1=1

        for i in range(2,n+1):
            ans=prev1+prev2
            prev2=prev1
            prev1=ans
        return prev1

