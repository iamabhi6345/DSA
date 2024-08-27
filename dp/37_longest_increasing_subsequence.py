"""  

Problem statement
For a given array with N elements, you need to find the length of the longest subsequence from the array such that all the elements of the subsequence are sorted in strictly increasing order.

Strictly Increasing Sequence is when each term in the sequence is larger than the preceding term.

For example:
[1, 2, 3, 4] is a strictly increasing array, while [2, 1, 4, 3] is not.
Detailed explanation ( Input/output format, Notes, Images )
Sample Input :
6
5 4 11 1 16 8
Sample Output 1 :
3
Explanation of Sample Input 1:
Length of longest subsequence is 3 i.e. [5, 11, 16] or [4, 11, 16].
Sample Input 2:
3
1 2 2
Sample Output 2 :
2

"""


from sys import stdin
import sys 
sys.setrecursionlimit(10**7)
import bisect

def longestIncreasingSubsequence(arr, n) :
    dp=[arr[0]]
    ans=1
    for i in range(n):
        if arr[i]>dp[-1]:
            dp.append(arr[i])
            ans+=1
        else:
            ind = bisect.bisect_left(dp ,arr[i] )
            dp[ind]= arr[i]
    return ans


#taking inpit using fast I/O
def takeInput() :
    n = int(input())
    if n==0 :
        return list(), n
    arr = list(map(int, stdin.readline().rstrip().split(" ")))
    return arr, n


#main
arr, n = takeInput()
print(longestIncreasingSubsequence(arr, n))

