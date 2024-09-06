class Solution:
    def power(self, x: float, n: int) -> float:
        
        if n == 1:
            return x

        if n == 0:
            return 1

        if n < 0:
            return 1 / self.power(x, -n)

        if n % 2 == 0:
            return self.power(x * x, n // 2)

        else:
            return x * self.power(x * x, n // 2)

    def myPow(self, x: float, n: int) -> float:
        return self.power(x, n)

sol= Solution()
print(sol.myPow(-2,1))
