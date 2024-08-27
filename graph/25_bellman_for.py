"""   

Given a weighted and directed graph of V vertices and E edges, Find the shortest distance of all the vertex's 
from the source vertex S. If a vertices can't be reach from the S then mark the distance as 10^8. Note: If the 
Graph contains a negative cycle then return an array consisting of only -1.

Example 1:

Input:

E = [[0,1,9]]
S = 0
Output:
0 9
Explanation:
Shortest distance of all nodes from
source is printed.
Example 2:

Input:

E = [[0,1,5],[1,0,3],[1,2,-1],[2,0,1]]
S = 2
Output:
1 6 0
Explanation:
For nodes 2 to 0, we can follow the path-
2-0. This has a distance of 1.
For nodes 2 to 1, we cam follow the path-
2-0-1, which has a distance of 1+5 = 6,
 

Your Task:
You don't need to read input or print anything. Your task is to complete the function bellman_ford( ) which 
takes a number of vertices V and an E-sized list of lists of three integers where the three integers are u,v, 
and w; denoting there's an edge from u to v, which has a weight of w and source node S as input parameters and 
returns a list of integers where the ith integer denotes the distance of an ith node from the source node.

If some node isn't possible to visit, then its distance should be 100000000(1e8). Also, If the Graph contains a 
negative cycle then return an array consisting of a single -1.

 

Expected Time Complexity: O(V*E).
Expected Auxiliary Space: O(V).

 

Constraints:
1 ≤ V ≤ 500
1 ≤ E ≤ V*(V-1)
-1000 ≤ adj[i][j] ≤ 1000
0 ≤ S < V


Time Complexity: O(V*E), where V = no. of vertices and E = no. of Edges.

Space Complexity: O(V) for the distance array which stores the minimized distances.

"""




#User function Template for python3

class Solution:
    # Function to construct and return cost of MST for a graph
    # represented using adjacency matrix representation
    '''
    V: nodes in graph
    edges: adjacency list for the graph
    S: Source
    '''
    def bellman_ford(self, V, edges, S):
        #code here
        dist =[int(1e8)]*V
        dist[S]=0
        for i in range(V-1):
            for i in edges:
                frm = i[0]
                to=i[1]
                wt = i[2]
                
                if ( dist[frm]!=1e8 and dist[frm] + wt < dist[to]):
                    dist[to] = dist[frm] + wt
                
        for i in edges:
                frm = i[0]
                to=i[1]
                wt = i[2]
                
                if ( dist[frm]!=1e8 and dist[frm] + wt < dist[to]):
                    return [-1]

        return dist

