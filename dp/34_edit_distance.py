"""  

Problem statement
You are given two strings 'S' and 'T' of lengths 'N' and 'M' respectively. Find the "Edit Distance" between 
the strings.

Edit Distance of two strings is the minimum number of steps required to make one string equal to the other. 
In order to do so, you can perform the following three operations:

1. Delete a character
2. Replace a character with another one
3. Insert a character
Note:
Strings don't contain spaces in between.
Detailed explanation ( Input/output format, Notes, Images )
Constraints:
0 <= N <= 10 ^ 3
0 <= M <= 10 ^ 3

Time Limit : 1sec
Sample Input 1 :
abc
dc
Sample Output 1 :
2
 Explanation For Sample Input 1 :
In 2 operations we can make the string T to look like string S. First, insert the character 'a' to string T, 
which makes it "adc".

And secondly, replace the character 'd' of the string T with 'b' from the string S. This would make string 
T to "abc" which is also the string S. Hence, the minimum distance.
Sample Input 2 :
whgtdwhgtdg
aswcfg
Sample Output 2 :
9

"""


from sys import stdin
import sys
sys.setrecursionlimit(10**7) 

def solve(i1 , i2 , s1 , s2, dp):
    if (i1<0):
        return i2+1
    if (i2<0):
        return i1+1
    
    if dp[i1][i2]!=-1:
        return dp[i1][i2]
    
    if (s1[i1] == s2[i2]):
        dp[i1][i2] = solve (i1-1 , i2-1 , s1 , s2 , dp)
        return dp[i1][i2]
    
    insert = 1+ solve(i1,i2-1,s1,s2,dp)
    delete = 1 + solve (i1-1 , i2 , s1 , s2 , dp)
    replace = 1+ solve(i1-1 , i2-1 , s1 , s2, dp)

    dp[i1][i2] = min(insert , min(delete , replace))
    return dp[i1][i2]



def editDistance(str1, str2) :
    
    # Your code goes here
    n1 = len(str1)
    n2 = len(str2)

    dp = [[-1]*n2 for _ in range(n1)]
    return solve(n1-1 , n2-1 , str1, str2 , dp)



#taking inpit using fast I/O
def takeInput() :
    str1=input()
    str2=input()

    return str1, str2


#main
str1, str2  = takeInput()
print(editDistance(str1, str2))
