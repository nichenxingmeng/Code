n = int(input().strip())
m = list(map(int, input().strip().split()))
dp = [0 for _ in range(n)]
max_ = 0

for i in range(n):
    dp[i] = 1
    for j in range(i):
        if m[i] >= m[j] and dp[i] < dp[j]+1:
            dp[i] = dp[j] + 1
    if dp[i] > max_:
        max_ = dp[i]
print(max_)
