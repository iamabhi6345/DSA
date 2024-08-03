def swap(arr , l ,r):
    tmp = arr[l]
    arr[l]=arr[r]
    arr[r]=tmp

def s(i,arr ):
    if (i>=len(arr)//2):
        return 
    n=len(arr)
    swap(arr, i, n-i-1)
    

def rev(l ):
    s(0,l)


l=[1,2,3,4  ]
rev(l)
print(l)
