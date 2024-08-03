"""  
    Problem statement
    You are given two positive integers 'n' and 'm'. You have to return the 'nth' root of 'm', i.e. 
    'm(1/n)'. If the 'nth root is not an integer, return -1.



    Note:
    'nth' root of an integer 'm' is a number, which, when raised to the power 'n', gives 'm' as a result.


    Example:
    Input: ‘n’ = 3, ‘m’ = 27

    Output: 3

    Explanation: 
    3rd Root of 27 is 3, as (3)^3 equals 27.


    Detailed explanation ( Input/output format, Notes, Images )
    Sample Input 1:
    3 27


    Sample Output 1:
    3


    Explanation For Sample Input 1:
    3rd Root of 27 is 3, as (3)^3 equals 27.


    Sample Input 2:
    4 69


    Sample Output 2:
    -1


    Explanation For Sample Input 2:
    4th Root of 69 is not an integer, hence -1.


    Expected Time Complexity:
    Try to do this in O(log(n+m)).


    Constraints:
    1 <= n <= 30
    1 <= m <= 10^9

    Time Limit: 1 sec.
"""




def NthRoot(n: int, m: int) -> int:
    # Write Your Code Here
    if(m==0)or (m==1) or (n==1):
        return n
    l=1
    h=m
    while(l<=h):
        mid=(l+h)//2
        ans=1
        for _ in range(n):
            ans=ans*mid
        if(ans==m):
            return mid
        if(ans>m):
            h=mid-1
        else:
            l=mid+1
    
    return -1


"""
    above are taking O(n) time for power calculation
    we can do binary exponentiation
"""

def pown(x,n):
    p=n
    if n<0:
        p=-1*n
    ans=1
    while(p>0):
        if(p%2==1):
            ans=ans*x
            p=p-1
        else:
            x=x*x
            p=p//2
    
    if (n<0):
        res= 1/ans
        return res 

    return ans
    


def NthRoot(n: int, m: int) -> int:
    # Write Your Code Here
    if(m==0)or (m==1) or (n==1):
        return n
    l=1
    h=m
    while(l<=h):
        mid=(l+h)//2
        ans=pown(mid,n)
        
        if(ans==m):
            return mid
        if(ans>m):
            h=mid-1
        else:
            l=mid+1
    
    return -1
