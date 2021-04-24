n = int(input().strip())
m = []
for i in range(n):
    m.append(list(map(int, input().strip().split())))
dp = []
for i in range(n):
    dp.append([0]*(i+1))
dp[0][0] = m[0][0]
for i in range(1, n):
    for j in range(len(m[i])):
        if j == 0:
            dp[i][j] = dp[i-1][j] + m[i][j]
        elif j == len(m[i]) - 1:
            dp[i][j] = dp[i-1][j-1] + m[i][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-1]) + m[i][j]
print(max(dp[n-1]))

