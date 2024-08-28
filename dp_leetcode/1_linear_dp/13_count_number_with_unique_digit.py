"""  
Given an integer n, return the count of all numbers with unique digits, x, where 0 <= x < 10n.

 

Example 1:

Input: n = 2
Output: 91
Explanation: The answer should be the total numbers in the range of 0 ≤ x < 100, excluding 11,22,33,44,55,66,77,88,99
Example 2:

Input: n = 0
Output: 1
 

Constraints:

0 <= n <= 8

"""

"""

for  3 digit number 
unique number
9 * 9 * 8
first digit cannot be zero so 9 choice
second can be zero but cannot be same as first so 9 choice
from third one 8 , 7, 6,....so on

"""


class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n==0:
            return 1
        dp=[0]*(n+1)
        dp[0]=1
        dp[1]=10
        for i in range(2,n+1):
            res=9
            t=9
            for j in range(1,i):
                res=res*t
                t=t-1
            dp[i]=res+dp[i-1]
        return dp[n]