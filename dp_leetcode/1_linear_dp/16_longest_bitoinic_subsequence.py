"""  
Problem statement
A Bitonic Sequence is a sequence of numbers that is first strictly increasing and then strictly decreasing.


A strictly ascending order sequence is also considered bitonic, with the decreasing part as empty, and same for a strictly descending order sequence.



For example, the sequences [1, 3, 5, 3, 2], [1, 2, 3, 4] are bitonic, whereas the sequences [5, 4, 1, 4, 5] and [1, 2, 2, 3] are not.



You are given an array 'arr' consisting of 'n' positive integers.



Find the length of the longest bitonic subsequence of 'arr'.



Example :
Input: 'arr' = [1, 2, 1, 2, 1]

Output: 3

Explanation: The longest bitonic subsequence for this array will be [1, 2, 1]. Please note that [1, 2, 2, 1] is not a valid bitonic subsequence, because the consecutive 2's are neither strictly increasing, nor strictly decreasing.
Detailed explanation ( Input/output format, Notes, Images )
Sample Input 1 :
5 
1 2 1 2 1


Sample Output 1:
3


Explanation For Sample Input 1:
The longest bitonic subsequence for this array will be [1, 2, 1]. Please note that [1, 2, 2, 1] is not a valid bitonic subsequence, because the consecutive 2's are neither strictly increasing, nor strictly decreasing.


Sample Input 2 :
5
1 2 1 3 4


Sample Output 2 :
4


Explanation For Sample Input 2:
The longest bitonic sequence for this array will be [1, 2, 3, 4].


Expected time complexity :
The expected time complexity is O(n ^ 2).


Constraints:
1 <= 'n' <= 10^3
1 <= 'arr[i]' <= 10^5

Time Limit: 1sec



find lcs from front  --->it will give increasing part
then find lcs from back  -->it will give decreasing part

then find  bitonc at index  increasing + decreasing -1 
-1 for common

then find max bitonic
"""




from typing import List

def longestBitonicSubsequence(arr: List[int], n: int) -> int:
 
    dp1=[1]*n
    dp2=[1]*n


    for i in range(n):
        for j in range(i):
            if arr[i]>arr[j] and 1+dp1[j]>dp1[i]:
                dp1[i]=1+dp1[j]

    for i in range(n-1 , -1,-1):
        for j in range(n-1 , i , -1):
            if (arr[i] > arr[j]) and 1+dp2[j] > dp2[i]:
                dp2[i] =dp2[j] + 1
                
    maxi =0
    for i in range(n):
        maxi = max( maxi , dp1[i]+dp2[i] -1 )
    
    return maxi
        