'''
n = int(input().strip())
m = []
for i in range(n):
    m.append([int(j) for j in input().strip().split()])
dp = [[0 for _ in range(n)] for _ in range(n)]
dp[0][0] = m[0][0]
sum_ = m[:]
for i in range(n):
    for j in range(1, n):
        sum_[i][j] = sum_[i][j-1] + sum_[i][j]

for i in range(1, n):
    dp[0][i] = max(dp[0][i-1] + m[0][i], m[0][i])
for i in range(1, n):
    dp[i][0] = max(dp[i-1][0] + m[i][0], m[i][0])

for i in range(1, n):
    for j in range(1, n):

        dp[i][j] = max(dp[i-1][j] + sum_[i][j], sum_[i][j])

ans = dp[0][0]
for i in range(n):
    temp = max(dp[i])
    if temp > ans:
        ans = temp
print(ans)
'''
n = int(input().strip())
matrix = []
for i in range(n):
    matrix.append([int(j) for j in input().strip().split()])
total = [[0 for _ in range(n)] for _ in range(n)]
arr = [0 for _ in range(n)]
dp = [0 for _ in range(n)]

def MaxSubquence(n):
    global arr, dp
    max_ = arr[0]
    for i in range(n):
        if i == 0:
            dp[i] = arr[i]
        else:
            dp[i] = max(dp[i-1] + arr[i], arr[i])
        max_ = max(max_, dp[i])
    return max_

def MaxSubtrix(n):
    global total, arr
    maximal = total[0][0]
    for i in range(n):
        for j in range(1, n):
            for k in range(n):
                if i == 0:
                    arr[k] = total[j][k]
                else:
                    arr[k] = total[j][k] - total[i-1][k]
            current = MaxSubquence(n)
            maximal = max(current, maximal)
    return maximal

for i in range(n):
    for j in range(n):
        if i == 0:
            total[i][j] = matrix[i][j]
        else:
            total[i][j] = total[i-1][j] + matrix[i][j]

ans = MaxSubmatrix(n)
print(ans)
