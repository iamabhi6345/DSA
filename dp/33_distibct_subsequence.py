""" 
Problem statement
A Subsequence of a string is the string that is obtained by deleting 0 or more letters from the string and 
keeping the rest of the letters in the same order.



We are given two strings, 'str' and 'sub'.



Find the number of subsequences of 'str' which are equal to 'sub'.



Since the answer can be very large, print it modulo 10 ^ 9 + 7.



Example :
Input: 'str' = “brootgroot” and 'sub' = “brt”

Output: 3

Explanation: The following subsequences formed by characters at given indices (0-based) of 'str' are 
equal to 'sub' :

str[0] = ‘b’, str[1] = ‘r’, str[4] = ‘t’

str[0] = ‘b’, str[1] = ‘r’, str[9] = ‘t’

str[0] = ‘b’, str[6] = ‘r’, str[9] = ‘t’
Detailed explanation ( Input/output format, Notes, Images )
Sample Input 1 :
brootgroot
brt


Sample Output 1 :
3


Explanation For Sample Input 1 :
The following subsequences formed by characters at given indices (0-based) of 'str' are equal to 'sub' :

str[0] = ‘b’, str[1] = ‘r’, str[4] = ‘t’

str[0] = ‘b’, str[1] = ‘r’, str[9] = ‘t’

str[0] = ‘b’, str[6] = ‘r’, str[9] = ‘t’


Sample Input 2 :
dingdingdingding
ing


Sample Output 2 :
20


Sample Input 3:
aaaaa
a


Sample Output 3:
5


Expected time complexity :
The expected time complexity is O(|str| * |sub|).


Constraints:
1 <= |str| <= 1000
1 <= |sub| <= 1000

Where |str| represents the length of the string 'str', and |sub| represents the length of the string 'sub'.

Time Limit: 1 sec.



?????????????????????????????

modulo gives float so use int 
"""




mod = 1e9+7

def solve(i1 , i2 , s1 , s2 , dp):
    if ( i2<0):
        return 1
    if (i1<0 ):
        return 0
    if dp[i1][i2]!=-1:
        return int(dp[i1][i2])
    
    if (s1[i1]==s2[i2]):
        take = (solve(i1-1 , i2-1 , s1 , s2 , dp))%mod
        nottake = (solve(i1-1 , i2, s1 , s2 , dp))%mod
        dp[i1][i2] = (take + nottake )%mod
        return int(dp[i1][i2])
    
    
    nottake = (solve(i1-1 , i2 , s1 , s2 , dp))%mod
    dp[i1][i2]=nottake
    return int(dp[i1][i2])
    

def distinctSubsequences(str: str, sub: str) -> int:
    # write your code here
    
    n1 = len(str)
    n2 = len(sub)

    dp = [[-1]*n2 for _ in range(n1)]
    return solve(n1-1 , n2-1 , str , sub , dp)