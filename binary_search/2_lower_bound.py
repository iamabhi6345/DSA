# lower bound = bisect_left 
def lowerBound1(arr: [int], n: int, x: int) -> int:
    # Write your code here
    low=0
    n =len(arr)
    high =n-1
    ans=n
    while (low<=high):
        mid=(low+high)//2
        if (arr[mid]>=x):
            ans=mid
            high=mid-1
        else:
            low=mid+1

    return ans


import bisect
def lowerBound(arr: [int], n: int, x: int) -> int:
    # Write your code here
    return bisect.bisect_left(arr,x)
