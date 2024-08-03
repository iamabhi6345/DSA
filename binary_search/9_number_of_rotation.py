def findKRotation(arr : [int]) -> int:
    # Write your code here.
    l=0
    h=len(arr)-1
    ans=1e9
    index=0
    while(l<=h):
        m=(l+h)//2
        if(arr[l]<=arr[m]):
            if(arr[l]<ans):
                print(ans," ",arr[l])
                ans=arr[l]
                index=l
            l=m+1
        
        else:
            if(arr[m]<ans):
                ans=arr[m]
                index=m
            h=m-1
    
    return index




print(findKRotation([2,3,4,1]))

# list=[1,2,3,4]
# print(list.__len__())
# print(list.__str__())
# print(list.__init__())
# print(list.__add__())