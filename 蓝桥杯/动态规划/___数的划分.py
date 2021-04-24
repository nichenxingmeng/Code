'''
n = int(input().strip())
dp = [[-1 for _ in range(n+1)] for _ in range(n+1)]

def solve(n, k):
    global dp
    if dp[n][k] != -1:
        return dp[n][k]
    if n < k:
        return 0
    if k == 1 or n == k:
        return 1
    dp[n][k] = solve(n-k, k) + solve(n-1, k-1)
    return dp[n][k]

ans = 0
for i in range(1, n+1):
    ans += solve(n, i)

print(ans)
'''
n = int(input().strip())

def solve(n):
    dp = [[0 for _ in range(n+1)] for _ in range(n+1)]

    for i in range(1, n+1):
        dp[i][1] = 1
        dp[i][i] = 1

    for i in range(3, n+1):
        for j in range(2, i):
            dp[i][j] = dp[i-1][j-1] + dp[i-j][j]

    total = 0
    for k in range(1, n+1):
        total += dp[n][k]
    return total

print(solve(n))
