s=set()

import sys 
n = int(input())
arr=list(map(int , sys.stdin.readline().rstrip().split(" "))) 
print(arr)
s = set(arr)
print(s)
ar2=list(s)
print(ar2)

l=-1e9
s=1e9
ansl=0
anss=0

for i in ar2:
    if i>l:
        ansl=l
        l=i
    if i<s:
        anss=s
        s=i

print(ansl , end=" ")
print(anss)
   