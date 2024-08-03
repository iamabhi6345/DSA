from typing import *

def searchInARotatedSortedArrayII(a : List[int], tar : int) -> bool:
    # Write your code here.
    l=0
    h=len(a)-1
    while(l<=h):
        mid=(l+h)//2
        if(a[mid]==tar):
            return True

        if(a[l]==[mid]) and (a[mid]==a[h]):
            l=l+1
            h=h-1
            continue
        
        if (a[l]<=a[mid]):
            if(tar >= a[l]) and (tar<=a[mid]):
                h=h-1
            else:
                l=l+1

        else:
            if(tar>=a[mid])and (tar<=a[h]):
                l=mid+1
            else:
                h=h-1
    return False    
        