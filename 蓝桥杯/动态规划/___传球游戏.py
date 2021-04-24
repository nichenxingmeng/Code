'''
n, m = map(int, input().strip().split())

start = 1
count = 0
def chuandi(n, m):
    global start, count
    if m == 0:
        if start == 1:
            count += 1
        return
    temp = start
    temp_ = m
    start -= 1
    if start == 0:
        start = n
    chuandi(n, m-1)
    start = temp
    m = temp_
    start += 1
    if start > n:
        start = 1
    chuandi(n,m-1)
    
chuandi(n, m)
print(count)
'''
n, m = map(int, input().strip().split())
dp = [[0 for _ in range(n)] for _ in range(m)]
dp[0][1] = 1
dp[0][n-1] = 1
for i in range(1, m):
    for j in range(n):
        if j == n-1:
            dp[i][j] = dp[i-1][j-1] + dp[i-1][0]
        else:
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]
print(dp[m-1][0])

