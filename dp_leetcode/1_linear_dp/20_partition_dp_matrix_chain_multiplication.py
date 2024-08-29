import sys

def solve(i, j, arr, dp):
    if i >= j:  
        return 0

    if dp[i][j] != -1:  
        return dp[i][j]

    mini = sys.maxsize 

    for k in range(i, j):

        steps = arr[i-1] * arr[k] * arr[j] + solve(i, k, arr, dp) + solve(k+1, j, arr, dp)
        mini = min(mini, steps)  

    dp[i][j] = mini  
    return dp[i][j]

def matrixMultiplication(arr, n):
    dp = [[-1] * n for _ in range(n)] 
    return solve(1, n-1, arr, dp)  

