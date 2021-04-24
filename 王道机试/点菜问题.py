m, n = map(int, input().strip().split())
v = [0 for _ in range(n)]
w = [0 for _ in range(n)]
for i in range(n):
    w[i], v[i] = map(int, input().strip().split())
dp = [0 for _ in range(m + 1)]

for i in range(n):
    for j in range(m, w[i]-1, -1):
        dp[j] = max(dp[j], dp[j - w[i]] + v[i])

print(dp[m])
