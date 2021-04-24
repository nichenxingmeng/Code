n = int(input().strip())
dp = [0 for _ in range(n+1)]
dp[1] = 1
if n == 1:
    print(dp[n])
elif n == 2:
    dp[2] = 2
    print(dp[n])
else:
    dp[2] = 2
    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    print(dp[n])
