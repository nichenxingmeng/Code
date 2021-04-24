n = int(input().strip())
m = list(map(int, input().strip().split()))
dp = [0 for _ in range(n)]
dp[0] = m[0]

for i in range(1, n):
    dp[i] = m[i]
    for j in range(i):
        if m[i] > m[j]:
            dp[i] = max(dp[i], dp[j]+m[i])

print(max(dp))
