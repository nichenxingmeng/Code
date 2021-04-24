n = int(input().strip())
m = list(map(int, input().strip().split()))
dp = [0 for _ in range(n)]
dp[0] = 1

for i in range(1, n):
    dp[i] = 1
    for j in range(i):
        if m[j] >= m[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))
