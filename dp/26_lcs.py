from sys import stdin


def solve(p1, p2, s, t, dp):
    if p1 < 0 or p2 < 0:
        return 0
    if dp[p1][p2] != -1:
        return dp[p1][p2]
    
    if s[p1] == t[p2]:
        dp[p1][p2] = 1 + solve(p1 - 1, p2 - 1, s, t, dp)
        return dp[p1][p2]
    
    l1 = solve(p1 - 1, p2, s, t, dp)
    l2 = solve(p1, p2 - 1, s, t, dp)
    dp[p1][p2] = max(l1, l2)
    return dp[p1][p2]


def lcs(s, t):
    n1 = len(s)
    n2 = len(t)
    dp = [[-1] * n2 for _ in range(n1)]
    return solve(n1 - 1, n2 - 1, s, t, dp)


s = str(stdin.readline().rstrip())
t = str(stdin.readline().rstrip())

print(lcs(s, t))
