"""  

Problem statement
You are given an array 'arr' of strings, where each string consists of English lowercase letters.



A string chain of 'arr' is defined as:

(1) A sequence of string formed using elements of 'arr'.

(2) Every string in the sequence can be formed by inserting a lowercase English letter into the previous string (except the first string).



Find the length of the longest possible string chain of 'arr'.



Example :
Input: 'arr' = ["x", "xx", "y", "xyx"] 

Output: 3

Explanation:
The longest possible string chain is “x” -> “xx” -> “xyx”.
The length of the given chain is 3, hence the answer is 3.


Detailed explanation ( Input/output format, Notes, Images )
Sample Input 1 :
3
m 
nm 
mmm


Expected Answer :
2


Output on console :
2


Explanation For Sample Input 1 :
In this testcase, the longest possible string chain is "m" -> "nm".
The length of the given chain is 2, hence the answer is 2.


Sample Input 2 :
5
a 
bc 
ad 
adc 
bcd


Expected Answer :
3


Output on console :
3


Explanation For Sample Input 2 :
In this testcase, the longest possible string chain is “a” -> “ad” -> “adc”.
The length of the given chain is 3, hence the answer is 3.


Expected Time Complexity :
Try to solve this in O(n*n*l), where 'n' is the size of array 'arr' and 'l' is the maximum length of a string in 'arr'. 


Constraints :
1 ≤ n ≤ 300    
1 ≤ arr[i].length ≤ 16

Time limit: 1 sec


"""


from typing import List

def check(s1 , s2):
    n1 = len(s1)
    n2 = len(s2)

    if (n1-n2!=1):
        return False 
    i=0
    j=0
    while(i<n1):
        if j<n2 and (s1[i]==s2[j]):
            i+=1
            j+=1
        else:
            i+=1
    
    if (i==n1 and j==n2):
        return True 
    return False 


def longestStrChain(arr: List[str]) -> int:
    arr.sort(key=len)
    n=len(arr)
    dp=[1]*n
    maxi=0


    for i in range(1 , n):
        for j in range(i):
            if check(arr[i],arr[j]) and 1+dp[j] >dp[i]:
                dp[i] = 1+ dp[j]

        if (dp[i] > maxi):
            maxi = dp[i]
    
    return maxi

