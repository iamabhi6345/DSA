def findMin(arr: [int]):
    # Write your code here.
    l=0
    h= len(arr)-1
    ans=1e9

    while(l<=h):
        m=(l+h)//2
        
        if(arr[l]<=arr[m]):
            ans=min(ans,arr[l])
            l=m+1
        else:
            ans=min(ans,arr[m])
            h=m-1
    return ans
        
