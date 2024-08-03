"""
    t(n) = 2t(n/2) + O(n)
    
    time complexity = O(nlog(n))
    space complexity = O(1)
    
"""

"""
from collections import deque
import time

# Create a large deque
d = deque(range(90000000))

# Measure the time to appendleft
print(d[0])
start_time = time.time()
d.appendleft(9090)
end_time = time.time()
print(d[0])
print("Time taken for appendleft:", end_time - start_time)  # Should be very small, indicating O(1)

"""

# from a_10_merge_sort import array1
class array:
    def __init__(self, arr):
        self.low = 0
        self.high = len(arr) - 1
        self.arr = arr
        # print(id(arr))
        # print(id(self.arr))
    
    def partition(self, arr, low, high) -> int:
        pivot = arr[low]
        i = low + 1
        j = high

        while True:
            while i <= j and arr[i] <= pivot:
                i += 1
            while i <= j and arr[j] > pivot:
                j -= 1
            if i <= j:
                arr[i], arr[j] = arr[j], arr[i]
            else:
                break
        
        arr[low], arr[j] = arr[j], arr[low]
        return j

    def quicksort(self, arr=None, low=None, high=None):
        if arr is None:
            arr = self.arr
        if low is None:
            low = self.low
        if high is None:
            high = self.high
        
        if low < high:
            # partition index
            pi = self.partition(arr, low, high)
            self.quicksort(arr, low, pi - 1)
            self.quicksort(arr, pi + 1, high)
    
    def print(self):
        print([i for i in self.arr])
 

# arr=[2,12,90,78,2,-8989,898,-9,8,-90]
arr=[4,2,5,1,3]
# print("id === ",id(arr))
a=array(arr)
a.print()
a.quicksort()
a.print()
print(arr)



# arr=[2,12,90,78,2,-8989,898,-9,8,-90]
# print("mergesort")        
# b= array1(arr)
# b.print()
# b.mergesort()
# b.print()
        
       
    