'''
k = int(input().strip())
dp = [[0 for _ in range(k+1)] for _ in range(k+1)]

for i in range(2, k+1):
    dp[i][2] = i * (i-1)

for i in range(3, k+1):
    for j in range(3, k+1):
        dp[i][j] = dp[i-1][j] + dp[i-1][j-1]

print(sum(dp[k]))
'''
k = int(input().strip())
ans = ((1 << k)-1-k)*2
print(ans)
