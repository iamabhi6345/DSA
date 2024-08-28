""" 
Problem statement
You are given an array of distinct numbers ‘arr’ of size 'n'.



Your task is to return the largest subset of numbers from ‘arr’, such that any pair of numbers ‘a’ and ‘b’ from the subset satisfies the following: a % b == 0 or b % a == 0.



A subset is nothing but any possible combination of the original array



Example:
Input: ‘arr’ = [1, 16, 7, 8, 4]

Output: [1, 4, 8, 16].

Explanation: In the set {1, 4, 8, 16}, you can take any pair from the set, and either one of the elements from the pair will divide the other.

There are other possible sets, but this is the largest one.
Detailed explanation ( Input/output format, Notes, Images )
Sample Input 1:
3
1 2 5
Sample Output 1 :
 Correct
Explanation of sample input 1:
The sets {1, 2} or {1, 5} are the two largest sets that satisfy the given condition.

Hence either of them could be the answer.
Sample Input 2:
 3
 3 3 3
Sample Output 2:
Correct
Explanation of sample input 2:
The set {3, 3, 3} is the largest set that satisfies the given condition.
Expected Time Complexity:
The expected time complexity is O(n^2).
Constraints:
1 <= N <= 5000
0 <= arr[i] <= 10^8    

Time Limit: 1 sec



????????????? divisible set , array chain , string chain first sort then make lis 
lis = longest increasing subsequence   

"""


from typing import List
from collections import deque


def divisibleSet(arr: List[int]) -> List[int]:
    arr.sort()


    maxi = 1
    last_index =0
    n=len(arr)
    hsh = list(range(n))
    dp=[1]*n
    for i in range(n):
        for j in range(i):
            if arr[i]%arr[j]==0 and 1+dp[j]>dp[i]:
                dp[i]=1+dp[j]
                hsh[i]=j

        if dp[i] > maxi:
            maxi=dp[i]
            last_index=i

    ans = deque()

    while(hsh[last_index]!=last_index):
        ans.appendleft(arr[last_index])
        last_index = hsh[last_index]

    ans.appendleft(arr[last_index])
    return ans
