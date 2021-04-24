n, m = map(int, input().strip().split())
dp = [[1 for _ in range(m + 1)] for _ in range(n + 1)]

for i in range(2, n + 1):
    for j in range(2, m + 1):
        if j <= i:
            dp[i][j] = dp[i - j][j] + dp[i][j - 1]
        else:
            dp[i][j] = dp[i][i]

print(dp[n][m])





































