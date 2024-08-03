def findPeakElement(arr: [int]) -> int:
    # Write your code here
    n=len(arr)
    if(n==1):
        return 0
    
    if(arr[0]>arr[1]):
        return 0
    
    if(arr[n-1]>arr[n-2]):
        return n-1
    
    l=1
    h=n-2

    while(l<=h):
        m=(l+h)//2
        if(arr[m]>arr[m-1]) and (arr[m]>arr[m+1]):
            return m    
        
        if (arr[m]>arr[m-1]):
            l=m+1
        else:
            h=m-1
    
    return -1

