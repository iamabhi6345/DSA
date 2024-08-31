from collections import deque
from typing import List
import sys
def bfs(graph: List[List[int]], start: int) -> List[int]:
    n = len(graph)
    dist = [float('inf')] * n
    dist[start] = 0
    queue = deque([start])
    
    while queue:
        u = queue.popleft()
        for v in graph[u]:
            if dist[v] == float('inf'):
                dist[v] = dist[u] + 1
                queue.append(v)
    
    return dist

def nearest_meeting_cell(n: int, edges: List[int], c1: int, c2: int) -> int:
    graph = [[] for _ in range(n)]
    for i, e in enumerate(edges):
        if e != -1:
            graph[i].append(e)
    
    dist_from_c1 = bfs(graph, c1)
    dist_from_c2 = bfs(graph, c2)
    
    min_dist = float('inf')
    min_node = -1
    
    for i in range(n):
        if dist_from_c1[i] != float('inf') and dist_from_c2[i] != float('inf'):
            total_dist = dist_from_c1[i] + dist_from_c2[i]
            if total_dist < min_dist:
                min_dist = total_dist
                min_node = i
    
    return min_node

# Input reading and function call
n = int(sys.stdin.readline().strip())
edges = list(map(int , sys.stdin.readline().strip().split(" ")))
c1, c2 = map(int, sys.stdin.readline().strip().split())
print(nearest_meeting_cell(n, edges, c1, c2))
