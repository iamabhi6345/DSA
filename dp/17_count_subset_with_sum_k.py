""" 
 
Problem statement
You are given an array 'arr' of size 'n' containing positive integers and a target sum 'k'.



Find the number of ways of selecting the elements from the array such that the sum of chosen elements is equal to the target 'k'.



Since the number of ways can be very large, print it modulo 10 ^ 9 + 7.



Example:
Input: 'arr' = [1, 1, 4, 5]

Output: 3

Explanation: The possible ways are:
[1, 4]
[1, 4]
[5]
Hence the output will be 3. Please note that both 1 present in 'arr' are treated differently.
Detailed explanation ( Input/output format, Notes, Images )
Sample Input 1 :
4 5
1 4 4 5


Sample Output 1 :
 3


Explanation For Sample Output 1:
The possible ways are:
[1, 4]
[1, 4]
[5]
Hence the output will be 3. Please note that both 1 present in 'arr' are treated differently.


Sample Input 2 :
3 2
1 1 1


Sample Output 2 :
3


Explanation For Sample Output 1:
There are three 1 present in the array. Answer is the number of ways to choose any two of them.


Sample Input 3 :
3 40
2 34 5


Sample Output 3 :
0


Expected time complexity :
The expected time complexity is O('n' * 'k').


Constraints:
1 <= 'n' <= 100
0 <= 'arr[i]' <= 1000
1 <= 'k' <= 1000

Time limit: 1 sec



"""

from typing import List

def solve(arr , k ):
    total = sum(arr)
    nr=len(arr)
    nc=k+1

    dp=[[0]*nc for _ in range(nr)]
    if arr[0]==0:
        dp[0][0]=2
    else:
        dp[0][0]=1


    if (arr[0]<=k):
        dp[0][arr[0]]=1

    for i in range(1, nr):
        for j in range(nc):
            nottaken = dp[i-1][j]
            taken= 0

            if ( arr[i]<=j):
                taken = dp[i-1][j-arr[i]]

            dp[i][j] = taken + nottaken 

    return dp 



def findWays(arr: List[int], k: int) -> int:
    # Write your code here.
    return solve(arr,k)[len(arr)-1][k]
