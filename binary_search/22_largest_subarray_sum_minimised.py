

""" 

Problem statement
Given an integer array ‘A’ of size ‘N’ and an integer ‘K'.



Split the array ‘A’ into ‘K’ non-empty subarrays such that the largest sum of any subarray is minimized.


Your task is to return the minimized largest sum of the split.



A subarray is a contiguous part of the array.


Example:
Input: ‘N’ = 5, ‘A’ = [1, 2, 3, 4, 5], ‘K’ = 3

Output: 6

Explanation: There are many ways to split the array ‘A’ into K consecutive subarrays. The best way to do this is to split the array ‘A’ into [1, 2, 3], [4], and [5], where the largest sum among the three subarrays is only 6.

Detailed explanation ( Input/output format, Notes, Images )
Sample Input 1:
5
1 2 3 4 5
3

Sample Output 1:
6

Explanation Of Sample Input 1:
Input: ‘N’ = 5, ‘A’ = [1, 2, 3, 4, 5], ‘K’ = 3

Output: 6

Explanation: There are many ways to split the array ‘A’ into K consecutive subarrays. 

The best way to do this is to split the array ‘A’ into [1, 2, 3], [4], and [5], where the largest sum among the three subarrays is only 6.

Sample Input 2:
3
3 5 1
3

Sample Output 2:
5

Explanation Of Sample Input 2:

Input: ‘N’ = 3, ‘A’ = [3, 5, 1], ‘K’ = 3

Output: 5

Explanation: There is only one way to split the array ‘A’ into 3 subarrays, i.e., [3], [5], and [1]. The largest sum among these subarrays is 5.

Sample Input 3:
6
10 4 5 10 9 10 
4

Sample Output 3:
15

Constraints:
1 <= N <= 1e4
1 <= A[i] <= 1e5
1 <= K <= N

Time Limit: 1-sec
Python (3.5)
123456789101112131415161718192021222324
def partition(a,lim):
    count=0
    i=0
    n=len(a)

    while(i<n):
        cap= lim
        while(i<n)and (a[i]<=cap):
            cap-=a[i]
            i+=1




"""  




def partition(a,lim):
    count=0
    i=0
    n=len(a)

    while(i<n):
        cap= lim
        while(i<n)and (a[i]<=cap):
            cap-=a[i]
            i+=1
        count+=1
    return count




def largestSubarraySumMinimized(a: [int], k: int) -> int:
    # Write Your Code Here
    l=max(a)
    h=sum(a)

    while(l<=h):
        mid =(l+h)//2
        if(partition(a,mid) > k):
            l=mid+1
        else:
            h=mid-1
    return l


