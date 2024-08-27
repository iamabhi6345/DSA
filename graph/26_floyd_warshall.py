"""

The problem is to find the shortest distances between every pair of vertices in a given edge-weighted directed graph. The graph is represented as an adjacency matrix of size n*n. Matrix[i][j] denotes the weight of the edge from i to j. If Matrix[i][j]=-1, it means there is no edge from i to j.
Note : Modify the distances for every pair in-place.

Examples :

Input: matrix = [[0, 25],[-1, 0]]

Output: [[0, 25],[-1, 0]]

Explanation: The shortest distance between every pair is already given(if it exists).
Input: matrix = [[0, 1, 43],[1, 0, 6],[-1, -1, 0]]

Output: [[0, 1, 7],[1, 0, 6],[-1, -1, 0]]

Explanation: We can reach 2 from 0 as 0->1->2 and the cost will be 1+6=7 which is less than 43.
Expected Time Complexity: O(n3)
Expected Space Complexity: O(1)

Constraints:
1 <= n <= 100
-1 <= matrix[ i ][ j ] <= 1000


Time Complexity: O(V3), as we have three nested loops each running for V times, where V = no. of vertices.

Space Complexity: O(V2), where V = no. of vertices. This space complexity is due to storing the adjacency matrix of the given graph.
"""



#User function template for Python

class Solution:
    def shortest_distance(self, matrix):
        n = len(matrix)
        
        # Initialize matrix: 0 for diagonal elements, large value for -1
        for i in range(n):
            for j in range(n):
                if i == j:
                    matrix[i][j] = 0
                elif matrix[i][j] == -1:
                    matrix[i][j] = float('inf')
        
        # Apply Floyd-Warshall algorithm to find shortest paths
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if matrix[i][k] != float('inf') and matrix[k][j] != float('inf'):
                        matrix[i][j] = min(matrix[i][j], matrix[i][k] + matrix[k][j])
        
        # Revert large values back to -1 for unreachable paths
        for i in range(n):
            for j in range(n):
                if matrix[i][j] == float('inf'):
                    matrix[i][j] = -1
