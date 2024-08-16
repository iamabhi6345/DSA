import sys

s1 = sys.stdin.readline().rstrip()
s2 = sys.stdin.readline().rstrip()

n1 = len(s1)
n2 = len(s2)

dp=[[0]*(n2+1) for _ in range(n1+1)]

for i in range(1,n1+1):
    for j in range(1,n2+1):
        if s1[i-1]==s2[j-1]:
            dp[i][j] = 1 + dp[i-1][j-1]
        else:
            dp[i][j] = max ( dp[i][j-1] , dp[i-1][j])


for i in range(len(dp)):
    print(dp[i])
    
ans = ""

i=n1
j=n2

while (i>0 and j>0):
        if s1[i-1] == s2[j-1]:
            ans = s1[i-1] + ans
            i = i-1
            j = j-1

        elif (dp[i-1][j] > dp[i][j-1]):
            i=i-1
        else:
            j=j-1

print(ans)
