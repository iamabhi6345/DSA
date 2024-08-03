"""   
        Problem statement
        You are given a sorted array ‘arr’ of ‘n’ numbers such that every number occurred twice in the array 
        except one, which appears only once.



        Return the number that appears once.



        Example:
        Input: 'arr' = [1,1,2,2,4,5,5]

        Output: 4 

        Explanation: 
        Number 4 only appears once the array.


        Note :
        Exactly one number in the array 'arr' appears once.


        Detailed explanation ( Input/output format, Notes, Images )
        Sample Input 1 :
        5 
        1 1 3 5 5 


        Sample Output 1 :
        3 
"""

def singleNonDuplicate(arr):
    # Write your code here
    # T.C of len = O(1)
    n=len(arr)
    if (n==1):
        return arr[0]
    if(arr[0]!=arr[1]):
        return arr[0]
    if(arr[n-1]!=arr[n-2]):
        return arr[n-1]
    
    l=1
    h=n-2

    while(l<=h):
        m=(l+h)//2
        if(arr[m]!=arr[m-1]) and (arr[m]!=arr[m+1]):
            return arr[m]

        # we are in left
        if((m%2==0) and arr[m]==arr[m+1]) or ((m%2==1) and (arr[m]==arr[m-1])):
            l=m+1
        #we are in right 
        else:
            h=m-1
    
    return -1



