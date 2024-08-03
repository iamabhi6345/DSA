from os import *
from sys import *
from collections import *
from math import *


def day(arr,c) -> int:
    d=0

    i=0
    while i <(len(arr)):
        cap=c
        while (i<len(arr)) and   (cap>=arr[i]):
            cap=cap-arr[i]
            i=i+1
        d=d+1
    return d

def leastWeightCapacity(w, d):
    # Write your code here.

    l=max(w)
    h=sum(w)



    while(l<=h):
        m=(l+h)//2
        if(day(w,m)  <=d):
            h=m-1
        else:
            l=m+1
    return l
        

# print(day([5 ,4 ,5 ,2 ,3, 4 ,5 ,6] , 17))
