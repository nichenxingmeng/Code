daodan = list(map(int, input().strip().split()))
max_ = 0
result = 0
dp = [0 for _ in range(len(daodan))]
dp[0] = 1
max_ = 1

for i in range(1, len(dp)):
    dp[i] = 1
    for j in range(i):
        if daodan[i] <= daodan[j] and dp[i] < dp[j]+1:
            dp[i] = dp[j]+1
    if max_ < dp[i]:
        max_ = dp[i]
print(dp)
print(max_)

while daodan:
    count = 0
    for i in range(len(daodan)):
        if i == 0:
            high = daodan[i]
            count += 1
            daodan[i] = -1
        else:
            if daodan[i] <= high:
                count += 1
                high = daodan[i]
                daodan[i] = -1
    if count > max_:
        max_ = count
    while -1 in daodan:
        daodan.remove(-1)
    result += 1
print(result)
