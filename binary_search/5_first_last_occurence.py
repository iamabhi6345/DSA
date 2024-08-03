import bisect

def firstAndLastPosition(arr, n, k):

    # Write your code here
    f= bisect.bisect_left(arr,k)
    if (f==len(arr)):
        return -1,-1

    if (arr[f]!=k):
        return -1,-1
    
    
    l= bisect.bisect_right(arr,k)

    return f, l-1