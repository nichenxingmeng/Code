from copy import deepcopy
n = int(input().strip())
m = []
for i in range(n):
    m.append([int(j) for j in input().strip().split()])

dp = deepcopy(m)
for i in range(n-2, -1, -1):
    for j in range(len(dp[i])):
        dp[i][j] = max(dp[i+1][j], dp[i+1][j+1]) + m[i][j]

print(dp[0][0])
    
