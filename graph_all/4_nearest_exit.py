""" 
1926. Nearest Exit from Entrance in Maze

You are given an m x n matrix maze (0-indexed) with empty cells (represented as '.') and walls (represented as '+'). You are also given the entrance of the maze, where entrance = [entrancerow, entrancecol] denotes the row and column of the cell you are initially standing at.

In one step, you can move one cell up, down, left, or right. You cannot step into a cell with a wall, and you cannot step outside the maze. Your goal is to find the nearest exit from the entrance. An exit is defined as an empty cell that is at the border of the maze. The entrance does not count as an exit.

Return the number of steps in the shortest path from the entrance to the nearest exit, or -1 if no such path exists.

 

Example 1:


Input: maze = [["+","+",".","+"],[".",".",".","+"],["+","+","+","."]], entrance = [1,2]
Output: 1
Explanation: There are 3 exits in this maze at [1,0], [0,2], and [2,3].
Initially, you are at the entrance cell [1,2].
- You can reach [1,0] by moving 2 steps left.
- You can reach [0,2] by moving 1 step up.
It is impossible to reach [2,3] from the entrance.
Thus, the nearest exit is [0,2], which is 1 step away.
Example 2:


Input: maze = [["+","+","+"],[".",".","."],["+","+","+"]], entrance = [1,0]
Output: 2
Explanation: There is 1 exit in this maze at [1,2].
[1,0] does not count as an exit since it is the entrance cell.
Initially, you are at the entrance cell [1,0].
- You can reach [1,2] by moving 2 steps right.
Thus, the nearest exit is [1,2], which is 2 steps away.
Example 3:


Input: maze = [[".","+"]], entrance = [0,0]
Output: -1
Explanation: There are no exits in this maze
"""


from collections import deque
class Solution:
    def __init__(self):
        self.directions=[(0,-1) , (1,0), (0,1), (-1,0)]
    def bfs(self , i , j , maze ):
        nr = len(maze)
        nc = len(maze[0])
        visited=[ [False]*nc for _ in range(nr)]
        visited[i][j]=True
        q=deque()
        for di , dj in self.directions:
            ni = i + di
            nj = j + dj

            if ( 0<=ni<nr) and ( 0<=nj<nc) and (maze[ni][nj]==".") and (visited[ni][nj]==False):
                q.append((1,ni,nj))
                visited[ni][nj]=True
        if not q:
            return -1
        
        while q:
            lvl , x , y = q.popleft()
            if x==0 or x==nr-1 or y==0 or y==nc-1:
                return lvl
            for di , dj in self.directions:
                ni = x + di
                nj = y + dj

                if ( 0<=ni<nr) and ( 0<=nj<nc) and (maze[ni][nj]==".") and (visited[ni][nj]==False):
                    q.append((lvl+1,ni,nj))
                    visited[ni][nj]=True

        return -1


    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        i = entrance[0]
        j = entrance[1]
        return self.bfs(i , j , maze)



# ?????????????????????????? solution-2 more space optimized

from collections import deque
class Solution:
    def __init__(self):
        self.directions=[(0,-1) , (1,0), (0,1), (-1,0)]
 

    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        i = entrance[0]
        j = entrance[1]
        nr=len(maze)
        nc=len(maze[0])
        # return self.bfs(i , j , maze)
        q = deque()
        q.append((1,i,j))
        maze[i][j]="+"
        while q:
            lvl , i , j = q.popleft()
            for di , dj in self.directions:
                ni = i + di
                nj = j + dj

                if ni==-1 or nj==-1 or ni==nr or nj ==nc:
                    continue
                if maze[ni][nj]=="+":
                    continue
                if ni==0 or ni==nr-1 or nj==0 or nj==nc-1:
                    return lvl

                maze[ni][nj]="+"
                q.append((lvl+1,ni,nj))

        return -1

