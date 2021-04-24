'''
n = int(input().strip())
dp = [[1 for _ in range(n + 1)] for _ in range(n + 1)]

for i in range(2, n + 1):
    for j in range(2, n + 1):
        if j <= i:
            dp[i][j] = dp[i - j][j] + dp[i][j - 1]
        else:
            dp[i][j] = dp[i][i]

print(dp[n][n])
'''
'''
n = int(input().strip())
dp = [[1 for _ in range(n + 1)] for _ in range(n + 1)]
i = 1
while i <=  n:
    for j in range(2, n + 1):
        if j <= i:
            dp[i][j] = (dp[i - j][j] + dp[i][j >> 1]) % 1000000000
        else:
            dp[i][j] = dp[i][i]
    i <<= 1

ans = i >> 1
temp = n - ans
k = ans >> 1
flag = True
while temp > 0:
    if temp >= k:
        flag = False
        for j in range(2, n + 1):
            dp[n][j] += dp[temp][j]
            dp[n][j] %= 1000000000
        temp -= k
    k >>= 1

if not flag:
    print((dp[n][n] + dp[ans][n] - 1) % 1000000000)
else:
    print((dp[ans][n]) % 1000000000)
'''
n = int(input().strip())
dp = [0 for _ in range(n + 1)]
dp[0] = dp[1] = 1

for i in range(2, n + 1):
    if i & 1:
        dp[i] = dp[i - 1]
    else:
        dp[i] = (dp[i - 1] + dp[i // 2]) % 1000000000

print(dp[n])
