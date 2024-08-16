""" 

https://atcoder.jp/contests/dp/tasks/dp_b
"""

import sys

def solve(ind, height, dp, k):
    if (ind==0):
        return 0
    if dp[ind]!=-1:
        return dp[ind]
    minstep=sys.maxsize
    for i in range(1,k+1):
        if(ind-i>=0):
            tmp=abs(height[ind]-height[ind-i]) + solve(ind-i,height,dp,k)
            minstep = min(minstep,tmp)
    dp[ind]=minstep
    return dp[ind]


def kjumps(arr,k):
    n=len(arr)
    dp=[-1]*n
    return solve(n-1,arr,dp,k)


print(kjumps([40, 10, 20 ,70, 80, 10 ,20, 70, 80, 60],4))
print(kjumps([30, 10, 60, 10, 60, 50],2))
print(kjumps([10 ,30 ,40, 50, 20],3))
print(kjumps([10 ,20,10],1))
print(kjumps([10 ,0],100))

                





#  tabulation



import sys

# Helper function to solve the problem using dynamic programming
def solve_util(n, height, dp, k):
    # Initialize the first element of the dp array as 0 since no steps are needed to reach the first position
    dp[0] = 0

    # Loop through the elements of the height array
    for i in range(1, n):
        mmSteps = sys.maxsize  # Initialize the minimum steps to a large value
        for j in range(1, k+1):
            if i - j >= 0:
                # Calculate the number of steps required to reach the current position from the previous positions
                jump = dp[i - j] + abs(height[i] - height[i - j])
                mmSteps = min(jump, mmSteps)  # Update the minimum steps
        dp[i] = mmSteps  # Store the minimum steps needed to reach the current position

    return dp[n-1]  # Return the minimum steps needed to reach the last position

# Main function to solve the problem
def solve2(n, height, k):
    dp = [-sys.maxsize] * n  # Initialize a dp array with large negative values
    return solve_util(n, height, dp, k)  # Call the helper function

# Entry point of the program
def main():
    height = [30, 10, 60, 10, 60, 50]
    n = len(height)
    k = 2
    dp = [-sys.maxsize] * n  # Initialize dp array
    result = solve2(n, height, k)  # Call the solve function
    print(result)  # Print the result

if __name__ == "__main__":
    main()

