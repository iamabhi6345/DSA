""" 

Contributed by
173 upvotes
Asked in companies
Problem statement
You are given an infinite supply of coins of each of denominations D = {D0, D1, D2, D3, ...... Dn-1}. You need to figure out the total number of ways W, in which you can make a change for value V using coins of denominations from D. Print 0, if a change isn't possible.

Detailed explanation ( Input/output format, Notes, Images )
Sample Input 1 :
3
1 2 3
4
Sample Output 1:
4
Explanation for Sample Output 1:
We can make a change for the value V = 4 in four ways.
1. (1,1,1,1), 
2. (1,1, 2), [One thing to note here is, (1, 1, 2) is same as that of (2, 1, 1) and (1, 2, 1)]
3. (1, 3), and 
4. (2, 2)
Sample Input 2 :
3
5 3 2
1
Sample Output 2:
0


"""





from sys import stdin,setrecursionlimit
setrecursionlimit(10**7)

def solve(ind , tar , dp , arr):
    if (tar==0):
        return 1
    if (ind==0):
        if(tar % arr[0]==0):
            return 1
        else:
            return 0
    if dp[ind][tar]!=-1:
        return dp[ind][tar]
    
    nottake = solve(ind-1 , tar , dp , arr)
    take =0
    if (arr[ind]<=tar):
        take = solve(ind  , tar-arr[ind] , dp , arr)
    
    dp[ind][tar] = take + nottake 
    return dp[ind][tar]

    

def countWaysToMakeChange(arr, value) :
    
	# Your code goes here
    nr = len(arr)

    dp=[[-1]*(value+1) for _ in range(nr)]
    return solve(nr-1 , value , dp , arr)


#taking inpit using fast I/O
def takeInput() :
    numDenominations = int(input())

    denominations = list(map(int, stdin.readline().strip().split(" ")))

    value = int(input())
    return denominations, numDenominations, value


#main
denominations, numDenomination, value = takeInput()
print((countWaysToMakeChange(denominations, value)))