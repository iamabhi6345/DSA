"""   

Alice and Bob take turns playing a game, with Alice starting first.

Initially, there is a number n on the chalkboard. On each player's turn, that 
player makes a move consisting of:

Choosing any x with 0 < x < n and n % x == 0.
Replacing the number n on the chalkboard with n - x.
Also, if a player cannot make a move, they lose the game.

Return true if and only if Alice wins the game, assuming both players play optimally.

 

Example 1:

Input: n = 2
Output: true
Explanation: Alice chooses 1, and Bob has no more moves.
Example 2:

Input: n = 3
Output: false
Explanation: Alice chooses 1, Bob chooses 1, and Alice has no more moves.
 

Constraints:

1 <= n <= 1000

"""


class Solution:
    def divisorGame(self, n: int) -> bool:
        return n%2==0


class Solution:
    def divisorGame(self, n: int) -> bool:
        # return n%2==0
        if n==1:
            return False
        dp=[False]*(n+1)

        for i in range(2,n+1):
            for x in range(1,i//2+1):
                if i%x==0:
                    if dp[i-x]==False:
                        dp[i]=True
        return dp[n]
        