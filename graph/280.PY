# # x=[2,5,6,7,9]
# x=[3,5,8,7,1,2]
# y = [7,7,6,4,8,9]

# import heapq

# q = []

# for i in range(len(x)):
#     heapq.heappush(q , (-y[i],x[i]))
# k=4
# for i in range(k):
#     print(heapq.heappop(q)[1] , end=" ")




lis= [1,2,3,4,1,2,78,65,3,67,65]
from collections import Counter
c = Counter(lis)
s= set()
for i in lis:
    if c[i]>1:
        s.add(i)
ans=list(s)
print(ans)