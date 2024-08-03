""" 
Problem statement
You are given 'n' roses and you are also given an array 'arr' where 'arr[i]' denotes that the 'ith' rose will bloom on the 'arr[i]th' day.



You can only pick already bloomed roses that are adjacent to make a bouquet. You are also told that you require exactly 'k' adjacent 
bloomed roses to make a single bouquet.



Find the minimum number of days required to make at least 'm' bouquets each containing 'k' roses. Return -1 if it is not possible.



Example :
Input: n = 9,  arr = [ 1, 2, 1, 2, 7, 2, 2, 3, 1 ], k = 3, m = 2

Output: 3. 

Explanation: This is because on the 3rd day: all the roses with 'arr[i]' less than equal to 3 have already bloomed, this means every rose 
except the 5th rose has bloomed. Now we can form the first bouquet from the first three roses and the second bouquet from the last three 
roses.
Detailed explanation ( Input/output format, Notes, Images )
Sample Input 1 :
9
1 2 1 2 7 2 2 3 1
3 2



Sample Output 1 :
3
Explanation For Sample Input 1 :
We will return 3, because:
All the roses with 'arr[i]' less than equal to 3 have already bloomed after 3 days, this means every rose except the 5th rose has bloomed. Now we can form the first bouquet from the first three roses and the second bouquet from the last three roses.



Sample Input 2 :
4
1 1 1 1
1 1
Sample Output 2 :
1




"""



from typing import List

def is_valid(arr,day,m,k):
    count=0
    nOfB=0

    for i in arr:
        if (i<=day):
            count = count +1
            if count==k:
                nOfB=nOfB+1
                count=0
        else:
            count=0
    
    return nOfB>=m


def roseGarden(arr: List[int], r: int, b: int):
    val=r*b
    n=len(arr)
    if val>n:
        return -1

    # write yur code here
    h = max(arr)
    l = min(arr)

 

    while(l<=h):
        m= (l+h)//2

        if(is_valid(arr,m,b,r)):
             h=m-1
        
        else:
            l=m+1
    
    return l
