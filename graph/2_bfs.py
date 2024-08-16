#User function Template for python3
"""   
Given a directed graph. The task is to do Breadth First Traversal of this graph 
starting from 0.
Note: One can move from node u to node v only if there's an edge from u to v. 
Find the BFS traversal of the graph starting from the 0th vertex, from left to right
according to the input graph. Also, you should only take nodes directly or
indirectly connected from Node 0 in consideration.




T.C =O(n) + O(2E)
2E is total degree
"""




from typing import List
from collections import deque
from queue import Queue
class Solution:
    #Function to return Breadth First Traversal of given graph.
    def bfsOfGraph(self, V: int, adj: List[List[int]]) -> List[int]:
        # code 
        queue=deque()
        queue.appendleft(0)
        ans=[]
        visited=[False]*V
        visited[0]=True

        while(len(queue)!=0):
            top=queue.pop()
            ans.append(top)
            for i in adj[top]:
                if(visited[i]==False):
                    queue.appendleft(i)
                    visited[i]=True
        return ans
            