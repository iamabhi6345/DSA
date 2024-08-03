"""
    t(n) = 2t(n/2) + O(n)
    
    time complexity = O(nlog(n))
    space complexity = O(n)
    
"""

class array:
    def __init__(self,arr):
        self.arr= arr
        self.low=0
        self.high=len(arr)-1
        self.mid = (self.low + (self.high - self.low) // 2)

    def merge(self,arr,low,mid,high):
        l=low
        r=mid+1
        tmp=[]

        while(l<=mid and r<=high):
            if (arr[l]<=arr[r]) :
                tmp.append(arr[l])
                l+=1
            else:
                tmp.append(arr[r])
                r+=1

        while(l<=mid):
            tmp.append(arr[l])
            l+=1

        while(r<=high):
            tmp.append(arr[r])
            r+=1
        
        for i in range(low,high+1,1):
            arr[i]=tmp[i-low]

    def mergesort(self, arr=None, low=None, high=None):
        if arr is None:
            arr = self.arr
        if low is None:
            low = self.low
        if high is None:
            high = self.high



        if low>=high:
            return

        mid = (low + high)//2
        self.mergesort(arr,low,mid)
        self.mergesort(arr,mid+1,high)
        self.merge(arr,low,mid,high)

    def print(self):
        print([i for i in self.arr])


if __name__ == "__main__":
    arr= array([2,12,90,78,2,-8989,898,-9,8,-90])
    print("before  sorting   ",end=" ")
    arr.print()
    arr.mergesort()
    print("after sorting   ",end="   ")
    arr.print()

