'''
n = int(input().strip())
m = list(map(int, input().strip().split()))
dp = [0 for _ in range(n)]
dp[0] = 1

for i in range(1, n):
    dp[i] = 1
    for j in range(i):
        if m[i] > m[j]:
            dp[i] = max(dp[i], dp[j]+1)
print(n - max(dp))
'''
n = int(input().strip())
m = list(map(int, input().strip().split()))
dp = [0 for _ in range(n)]
dp[0] = 1

for i in range(1, n):
    dp[i] = 1
    for j in range(i):
        if m[i] > m[j]:
            dp[i] = max(dp[i], dp[j]+1)
dp_ = dp[:]
dp = [0 for _ in range(n)]

for i in range(1, n):
    for j in range(i):
        if m[i] < m[j]:
            dp[i] = max(dp[i], dp[j]+1)

for i in range(n):
    dp[i] += dp_[i]

print(max(dp))
