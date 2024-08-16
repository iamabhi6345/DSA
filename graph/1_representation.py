"""


import sys

a,b=map(int,sys.stdin.readline().rstrip().split(" "))

# list = list(map(int,sys.stdin.readline().rstrip().split(" ")))
# print(list)
graph= [[0]*(a+1) for _ in range(a+1)]
for _ in range(b):
    n1,n2=map(int,sys.stdin.readline().rstrip().split(" "))
    graph[n1][n2]=1
    graph[n2][n1]=1

print(graph)


""" 
    


"""  
    method 2 
    adjacency matrix
"""

import sys
a,b =map(int,sys.stdin.readline().rstrip().split(" "))
graph = {i:set() for i in range(1,a+1)}
for _ in range(1,b+1):
    n1,n2=map(int,sys.stdin.readline().rstrip().split(" "))
    graph[n1].add(n2)
    graph[n2].add(n1)

for vertex in sorted(graph):
    adjacent_vertices = sorted(graph[vertex])
    print(f"{vertex}: {' '.join(map(str, adjacent_vertices))}")

