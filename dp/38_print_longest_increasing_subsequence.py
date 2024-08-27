from sys import stdin
import sys 
sys.setrecursionlimit(10**7)
from collections import deque

def longestIncreasingSubsequence(arr, n) :

    dp=[1]*n
    hsh=list(range(n))
    ans=1
    last_index=0
    dq=deque()

    for i in range(1,n):

        for j in range(i):
            if arr[i]>arr[j]  and (1+dp[j]) > dp[i]:
                dp[i] = 1+ dp[j]
                hsh[i] = j
        if ( dp[i]>ans):
            ans=dp[i]
            last_index=i
    # return ans
    
    while(hsh[last_index]!=last_index):
        dq.appendleft(arr[last_index])
        last_index = hsh[last_index]
    dq.appendleft(arr[last_index])


    return dq


#taking inpit using fast I/O
def takeInput() :
    n = int(input())
    if n==0 :
        return list(), n
    arr = list(map(int, stdin.readline().strip().split(" ")))
    return arr, n

arr, n = takeInput()
print(list(longestIncreasingSubsequence(arr, n)))



# 5
# 1000 78 90 98 99 100

