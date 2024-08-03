""" 
    one half will always be sorted so just decide which part will be sorted
    
    it works only when if there are unique elements only
    
    
    not working example
        [3 , 1 , 2 , 3, 3 , 3 , 3 ]
        
    moto was to sort by deciding which part is  sorted
    low=3,mid=3,high-=3
    now cannot say which part is sorted so fomany elements 
    
    problem occured when arr[low] = arr[mid] =  arr[high]
    
    solution is to make trim searchspace
"""

def search(arr, n, k):
    
    # Write your code here
	
    l=0
    h=n-1

    while(l<=h):
        mid=(l+h)//2
        if( arr[mid]==k):
            return mid
        
        # check if left half is sorted
        if(arr[low]<=arr[mid]):
            if(k>=arr[low]) and (k<=arr[mid]):
                high=mid-1
            else:
                low=mid+1
        
        else:
            if(k>=arr[mid]) and (k<=arr[high]):
                low=mid+1
            else:
                high=mid-1
    return -1





