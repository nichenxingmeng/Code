n, k = map(int, input().strip().split())
temp = [1 for _ in range(k)]
result = [1 for _ in range(k)]
dp = [0 for _ in range(10000)]
max_ = -9999

def dfs(x):
    if x == k:
        panduan()
        return
    for i in range(temp[x-1]+1, temp[x-1]*n+2):
        temp[x] = i
        dfs(x+1)

def panduan():
    global max_
    i = 0
    while dp[i] <= n:
        i += 1
        dp[i] = i
        for j in range(k):
            if temp[j] <= i:
                dp[i] = min(dp[i], dp[i-temp[j]]+1)
        if i-1 > max_:
            max_ = i-1
            for xy in range(k):
                result[xy] = temp[xy]

dfs(1)
for i in range(k):
    print(result[i], end=' ')
print()
print(f'MAX={max_}')
