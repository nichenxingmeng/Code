'''
n, m = map(int, input().strip().split())
ai = list(map(int, input().strip().split()))
temp = []
for i in range(n):
    temp.append([x for x in range(ai[i]+1)])
temp_ = [[] for _ in range(n-1)]

for i in range(n-1):
    for j in range(len(temp[i])):
        for k in range(len(temp[i+1])):
            if temp[i][j] + temp[i+1][k] > m:
                break
            else:
                temp_[i].append(temp[i][j] + temp[i+1][k])
    temp[i+1] = temp_[i][:]
count = 0
for i in range(len(temp_[-1])):
    if temp_[-1][i] == m:
        count += 1
        count %= 1000007
print(count%1000007)
'''
n, m = map(int, input().strip())
hua = list(map(int, input().strip().split()))
dp = [[0]*(m+1) for _ in range(n+1)]

for j in range(hua[0]+1):
    dp[1][j] = 1
for i in range(1, n+1):
    dp[i][0] = 1
for i in range(2, n+1):
    for j in range(1, m+1):
        for k in range(hua[i-1]+1):
            if j-k >= 0:
                dp[i][j] = (dp[i][j] + dp[i-1][j-k])%1000007
    print(dp)
print(dp[n][m])
