""" 
There are n rooms labeled from 0 to n - 1 and all the rooms are locked except for room 0. Your goal is to visit all the rooms. However, you cannot enter a locked room without having its key.

When you visit a room, you may find a set of distinct keys in it. Each key has a number on it, denoting which room it unlocks, and you can take all of them with you to unlock the other rooms.

Given an array rooms where rooms[i] is the set of keys that you can obtain if you visited room i, return true if you can visit all the rooms, or false otherwise.

 

Example 1:

Input: rooms = [[1],[2],[3],[]]
Output: true
Explanation: 
We visit room 0 and pick up key 1.
We then visit room 1 and pick up key 2.
We then visit room 2 and pick up key 3.
We then visit room 3.
Since we were able to visit every room, we return true.
Example 2:

Input: rooms = [[1,3],[3,0,1],[2],[0]]
Output: false
Explanation: We can not enter room number 2 since the only key that unlocks it is in that room.
 
 
"""


class Solution:
    def dfs(self ,start ,adj , vis):
        vis[start]=True
        for node in adj[start]:
            if vis[node]==False:
                vis[node]=True
                self.dfs(node , adj , vis)
                    
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n=len(rooms)
        adj=[ [] for _ in range(n)]
        for i in range(n):
            for j in rooms[i]:
                adj[i].append(j)
        
        vis=[False]*n
        self.dfs(0,adj,vis)
        for x in vis:
            if x==False:
                return False
        return True
