"""
886. Possible Bipartition
Solved
Medium
Topics
Companies
We want to split a group of n people (labeled from 1 to n) into two groups of any size. Each person may dislike some other people, and they should not go into the same group.

Given the integer n and the array dislikes where dislikes[i] = [ai, bi] indicates that the person labeled ai does not like the person labeled bi, return true if it is possible to split everyone into two groups in this way.

 

Example 1:

Input: n = 4, dislikes = [[1,2],[1,3],[2,4]]
Output: true
Explanation: The first group has [1,4], and the second group has [2,3].
Example 2:

Input: n = 3, dislikes = [[1,2],[1,3],[2,3]]
Output: false
Explanation: We need at least 3 groups to divide them. We cannot put them in two groups.
 

Constraints:

1 <= n <= 2000
0 <= dislikes.length <= 104
dislikes[i].length == 2
1 <= ai < bi <= n
All the pairs of dislikes are unique.


see example it is 1 indexing
"""


from collections import deque
class Solution:
    def bfs(self , start , n  , adj , color):
        
        q=deque()
        q.append(start)
        color[start]=0
        while q:
            top=q.popleft()
            for i in adj[top]:
                if color[i]==-1:
                    q.append(i)
                    color[i]=1-color[top]
                elif color[i]==color[top]:
                    return False
        return True



    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        adj = [ [] for _ in range(n+1)]

        for i,j in dislikes:
            adj[i].append(j)
            adj[j].append(i)
        
        color= [-1]*(n+1)

        for i in range(1,n+1):
            if color[i]==-1:
                if self.bfs(i,n,adj,color)==False:
                    return False
        return True
