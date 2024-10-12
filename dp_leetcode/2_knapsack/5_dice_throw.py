"""  
GFG
Dice throw
Difficulty: MediumAccuracy: 36.52%Submissions: 34K+Points: 4
Given n dice each with m faces. Find the number of ways to get sum x which is the summation of values on each face when all the dice are thrown.

Example:

Input: m = 6, n = 3, x = 12
Output: 25
Explanation: There are 25 total ways to get the Sum 12 using 3 dices with faces from 1 to 6.
Input: m = 2, n = 3, x = 6
Output: 1
Explanation: There is only 1 way to get the Sum 6 using 3 dices with faces from 1 to 2. All the dices will have to land on 2.
Expected Time Complexity: O(m*n*x)
Expected Auxiliary Space: O(n*x)

Constraints:
1 <= m,n,x <= 50

"""

# ?????????????????tabulation   

class Solution:
    def solve_tab(self , dice , face , target):
        dp=[  [0]*(target+1)  for _ in range(dice+1)]
        
        dp[0][0]=1
        
        for i in range(1 , dice+1):
            for j in range(1 , target+1):
                ans = 0
                for k in range(1 , face +1):
                    if j-k>=0:
                        ans = ans + dp[i-1][j-k]
                
                dp[i][j]=ans
        return dp[dice][target]
        
    def noOfWays(self, m,n,x):
        # code here
        return self.solve_tab(n,m,x)


# ????????????????????????? memoization  

#User function Template for python3

class Solution:
    def solve(self , dice , face , target,dp):
        if target <0:
            return 0
        if dice==0 and target!=0:
            return 0
        if target==0 and dice!=0:
            return 0
        if dice==0 and target==0:
            return 1
        if dp[dice][target] !=-1:
            return dp[dice][target]
        
        ans=0
        for i in range(1 , face+1):
            ans = ans + self.solve(dice-1 , face , target-i,dp)
        dp[dice][target] = ans
        return ans
    def noOfWays(self, m,n,x):
        # code here
        # dp={}
        dp=[ [-1]*(x+1)  for _ in range(n+1)  ]
        return self.solve(n , m , x,dp)
        


# ?????????? memoization + dictionary instead of 2-d  array 
#User function Template for python3

class Solution:
    def solve(self , dice , face , target,dp):
        if target <0:
            return 0
        if dice==0 and target!=0:
            return 0
        if target==0 and dice!=0:
            return 0
        if dice==0 and target==0:
            return 1
        if (dice , target) in dp:
            return dp[(dice,target)]
        
        ans=0
        for i in range(1 , face+1):
            ans = ans + self.solve(dice-1 , face , target-i,dp)
        dp[(dice,target)] = ans
        return ans
    def noOfWays(self, m,n,x):
        # code here
        dp={}
        return self.solve(n , m , x,dp)
        




# ????????????????? recurion


#User function Template for python3

class Solution:
    def solve(self , dice , face , target):
        if target <0:
            return 0
        if dice==0 and target!=0:
            return 0
        if target==0 and dice!=0:
            return 0
        if dice==0 and target==0:
            return 1
        
        ans=0
        for i in range(1 , face+1):
            ans = ans + self.solve(dice-1 , face , target-i)
        return ans
    def noOfWays(self, m,n,x):
        # code here
        return self.solve(n , m , x)
        
