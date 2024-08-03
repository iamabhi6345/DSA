"""  
    There are n friends that are playing a game.The friends are sitting in a circle and are numbered from 1 to n
    in clockwise order. More formally, moving clockwise from the ith friend brings you to the (i+1)th friend
    for 1 <= i < n, and moving clockwise from the nth friend brings you to the 1st friend.

    The rules of the game are as follows:

        Start at the 1st friend.
        Count the next k friends in the clockwise direction including the friend you started at. 
        The counting wraps around the circle and may count some friends more than once.
        The last friend you counted leaves the circle and loses the game.
        If there is still more than one friend in the circle, go back to step 2 starting from the friend immediately clockwise of the friend who just lost and repeat.
        Else, the last friend in the circle wins the game.

    Given the number of friends, n, and an integer k, return the winner of the game.
"""
    
    
    
    
# -----------------------------------------------------------------------------------------------

class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        l=[]
        for i in range(n):
            l.append(i+1)
        
        return (self.helper(l,0,k))
        
    
    def helper(self,l,curr,k):
        if len(l)==1:
            return l[0]
        next = (curr + k -1)%(len(l))
        l.pop(next)
        curr= next
        return (self.helper(l,curr,k))

# ---------------------------------------------------------------------------------------------------------------------------


"""  
 why to write  cur_ind= next_to_remove 
 initial list = [1 , 2,3 4, 5]
 k=2 , current index =0 , index_to_remove = (0 + 2 -1)%5 =1  (we write "k-1"  qki we have to count itself as well)
 
 so index 1 ,,(value 2) will be removed and new pointer will be at 3
 but in new list = [1,3,4,5]
 index of 3 =1 
 index of new starting is same as that has been removed 
 
 so current index = index_to_remove ------(after pop)

 
"""

def findTheWinner1( n: int, k: int) -> int:
        l=[]
        for i in range(n):
            l.append(i+1)
        
        cur_ind=0

        while len(l)!=1:
            next_to_remove = (cur_ind + k - 1)% (len(l))
            l.pop(next_to_remove)
            cur_ind= next_to_remove           
        return l[0]
    
print(findTheWinner1(5,2))