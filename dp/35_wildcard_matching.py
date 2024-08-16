"""   

Given a text and a wildcard pattern of size N and M respectively, implement a wildcard pattern matching algorithm that finds if the wildcard pattern is matched with the text. The matching should cover the entire text not partial text.

The wildcard pattern can include the characters ‘?’ and ‘*’

 ‘?’ – matches any single character 
 ‘*’ – Matches any sequence of characters(sequence can be of length 0 or more)
Detailed explanation ( Input/output format, Notes, Images )
Constraints:
1 <= T <= 100
1 <= N <= 200
1 <= M <= 200

Where 'N' denotes the length of 'TEXT' and 'M' denotes the length of 'PATTERN'.

'TEXT' and 'PATTERN' contain only lowercase letters and patterns may contain special characters ‘*’ and ‘?’

Time Limit: 1sec
Sample Input 1:
3
?ay
ray
ab*cd
abdefcd
ab?d
abcc
Sample Output 1:
True
True
False
Explanation of the Sample Input1:
Test Case 1:
The pattern is “?ay” and the text is ray.
‘?’ can match a character so it matches with a character ‘r’ of the text and rest of the text matches with the pattern so we print True.

Test Case 2:
“ab” of text matches with “ab” of pattern and then ‘*’ of pattern matches with “def” of the text and “cd” of text matches with “cd” of the pattern. Whole text matches with the pattern so we print True.

Test Case 3:
“ab” of pattern matches with “ab” of text. ‘?’ of pattern matches with ‘c’ of the text but ‘d’ of the pattern do not match with ‘c’ of the text so we print False.
Sample Input 1:
1
ba*a?
baaabab
Sample Output 1:
True

"""



# def is_all_star(str  , i):
#     for j in range(i+1):
#         if str[j]!="*":
#             return False
    
#     return True

# def solve(i , j , s1 , s2 , dp):
#     if i<0 and j <0:
#         return True 
#     if i<0 and j>=0:
#         return False
#     if i>=0 and j<0:
#         return is_all_star(s1 , i)

#     if dp[i][j]!=-1:
#         return dp[i][j]
    
#     if s1[i]==s2[j]  or  s1[i]=='?':
#         dp[i][j] = solve(i-1 , j-1 , s1, s2 , dp)
#         return dp[i][j]
    
#     elif s1[i]=="*":
#         dp[i][j] = solve(i-1, j , s1 , s2  , dp) or solve(i,j-1,s1,s2,dp)
#         return dp[i][j]
    
#     dp[i][j]=False
#     return dp[i][j]


# def wildcardMatching(pattern, text):
#     # Write your code here.
#     n1 = len(pattern)
#     n2= len(text)

#     dp=[[-1]*n2 for _ in range(n1)]

#     return solve (n1-1 , n2-1 , pattern , text , dp)


# t=int(input())

# while t>0:

#     pattern=input()
#     text=input()

#     print(wildcardMatching(pattern,text))
    
#     t-=1





def is_all_star(s, i):
    """ Check if all characters from 0 to i in s are '*' """
    for j in range(i + 1):
        if s[j] != '*':
            return False
    return True

def solve(i, j, s1, s2, dp):
    """ Recursive function with memoization for wildcard matching """
    if i < 0 and j < 0:
        return True
    if i < 0 and j >= 0:
        return False
    if i >= 0 and j < 0:
        return is_all_star(s1, i)

    if dp[i][j] != -1:
        return dp[i][j]

    if s1[i] == s2[j] or s1[i] == '?':
        dp[i][j] = solve(i - 1, j - 1, s1, s2, dp)
    elif s1[i] == '*':
        dp[i][j] = solve(i - 1, j, s1, s2, dp) or solve(i, j - 1, s1, s2, dp)
    else:
        dp[i][j] = False

    return dp[i][j]

def wildcardMatching(pattern, text):
    """ Wrapper function for wildcard matching """
    n1 = len(pattern)
    n2 = len(text)

    # Initialize DP table with -1 (uncomputed)
    dp = [[-1] * n2 for _ in range(n1)]
    
    return solve(n1 - 1, n2 - 1, pattern, text, dp)

# Input and processing
t = int(input())

while t > 0:
    pattern = input().strip()
    text = input().strip()

    print(wildcardMatching(pattern, text))

    t -= 1
