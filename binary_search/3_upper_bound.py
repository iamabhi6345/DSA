# upper bound= bisect_right 

"""   
    time complexity of all bisect algorithm is log(n)
    because it follows binarysearch
    
"""
def upperBound1(arr: [int], x: int, n: int) -> int:
    # Write your code here.
 
    low=0
    n =len(arr)
    high =n-1
    ans=n
    while (low<=high):
        mid=(low+high)//2
        if (arr[mid]>x):
            ans=mid
            high=mid-1
        else:
            low=mid+1

    return ans




import bisect
def upperBound(arr: [int], x: int, n: int) -> int:
    # Write your code here.
 
    return bisect.bisect_right(arr,x)


