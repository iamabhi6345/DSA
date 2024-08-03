"""   
        Problem statement
        You are given a strictly increasing array 'vec' and a positive integer 'k'.



        Find the 'kth' positive integer missing from 'vec'.



        Example :
        Input: vec = [2,4,5,7] , k = 3

        Output: 6

        Explanation : 
        
        In the given example, first missing positive integer is 1 second missing positive integer is 3,
        and the third missing positive integer is 6.
        Hence the answer is 6. 


        Detailed explanation ( Input/output format, Notes, Images )
        Sample Input 1 :
        4
        4 7 9 10
        1


        Sample Output 1 :
        1


        Explanation For Sample Input 1 :
        The missing numbers are 1, 2, 3, 5, 6, 8, 11, 12, ……, and so on.
        Since 'k' is 1, the first missing element is 1.


        Sample Input 2 :
        4
        4 7 9 10
        4

        Sample Output 2 :
        5


        Expected Time Complexity :
        Try to solve it in O(log(n)).
        Constraints :
        1 <= 'n' <= 10 ^ 4
        1 <= 'k' <= 10 ^ 9
        -10 ^ 9 <= 'vec[i]' <= 10 ^ 9

        Time Limit : 1 sec



"""






from typing import List

def missingK(arr: List[int], n: int, k: int) -> int:
    # Write your code here.
    if (k < arr[0]):
        return k
    
    l=0
    h=len(arr)-1

    while(l<=h):
        m=(l+h)//2
        miss_up_to_m = arr[m]-(m+1)

        if    miss_up_to_m >=k  :
            h=m-1
        else:
            l=m+1
    

    ans= arr[h]  + (k - (  arr[h] - (h+1) ))
    return ans
