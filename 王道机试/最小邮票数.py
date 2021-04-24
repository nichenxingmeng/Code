'''
n = int(input().strip())
youpiao = list(map(int, input().strip().split()))
dp = [0 for _ in range(n + 1)]

dp[1] = 1
for i in range(2, n+1):
    if i in youpiao:
        dp[i] = 1
    else:
        dp[i] = i
    for j in range(len(youpiao)):
        if youpiao[j] <= i:
            dp[i] = min(dp[i], dp[i - youpiao[j]] + 1)

print(dp[n])
'''
m = int(input().strip())
n = int(input().strip())
youpiao = list(map(int, input().strip().split()))
dp = [_ for _ in range(m + 1)]

for i in range(n):
    for j in range(m, youpiao[i] - 1, -1):
        dp[j] = min(dp[j], dp[j - youpiao[i]] + 1)

print(dp[m])
