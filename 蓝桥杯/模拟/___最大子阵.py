'''
from copy import deepcopy
n, m = map(int, input().strip().split())
A = []
for i in range(n):
    A.append([int(j) for j in input().strip().split()])

dp = [[0 for _ in range(m)] for _ in range(n)]
dp[0][0] = A[0][0]

for i in range(1, n):
    dp[i][0] = max(dp[i-1][0] + A[i][0], A[i][0])
for j in range(1, m):
    dp[0][j] = max(dp[0][j-1] + A[0][j], A[0][j])

sum_ = deepcopy(A)
for i in range(1, n):
    for j in range(1, m):
        sum_[i][j] = sum_[i][j-1] + A[i][j]

for i in range(1, n):
    for j in range(1, m):
        dp[i][j] = max(dp[i-1][j] + sum_[i][j], sum_[i][j])

ans = A[0][0]
for i in range(n):
    temp = max(dp[i])
    if temp > ans:
        ans = temp
for i in range(n):
    print(' '.join(map(str, dp[i])))
print(ans)
'''
n, m = map(int, input().strip().split())
A = []
for i in range(n):
    A.append([int(j) for j in input().strip().split()])
sum_ = [[0 for _ in range(m)] for _ in range(n)]
temp = [0 for _ in range(m)]
dp = [0 for _ in range(m)]

def Maxdp(m):
    global dp, temp
    dp[0] = temp[0]
    for i in range(1, m):
        dp[i] = max(dp[i-1] + temp[i], temp[i])
    return max(dp)

def Maxtemp(n, m):
    global temp, sum_
    max_ = 0
    for i in range(n):
        for j in range(i, n):
            for k in range(m):
                if i == 0:
                    temp[k] = sum_[j][k]
                else:
                    temp[k] = sum_[j][k] - sum_[i-1][k]
            current = Maxdp(m)
            max_ = max(max_, current)
    return max_

for i in range(n):
    for j in range(m):
        if i == 0:
            sum_[i][j] = A[i][j]
        else:
            sum_[i][j] = sum_[i-1][j] + A[i][j]

ans = Maxtemp(n, m)
print(ans)
        
