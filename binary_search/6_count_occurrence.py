import bisect
def count(arr: [int], n: int, x: int) -> int:
    # Your code goes here
    l=bisect.bisect_left(arr,x)

    if (l==n):
        return 0
    
    count=0
    if(arr[l]!=x):
        return 0
    
    r=bisect.bisect_right(arr,x)
    return (r-l)