from copy import deepcopy
num = int(input().strip())
while num > 0:
    n = int(input().strip())
    m = []
    for i in range(2 * n - 1):
        m.append([int(j) for j in input().strip().split()])
    dp = deepcopy(m)
    
    for i in range(2 * n - 3, n - 2, -1):
        for j in range(len(dp[i])):
            if j == 0:
                dp[i][j] = dp[i + 1][j] + m[i][j]
            elif j == len(dp[i]) - 1:
                dp[i][j] = dp[i + 1][-1] + m[i][j]
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i + 1][j - 1]) + m[i][j]

    for i in range(n - 2, -1, -1):
        for j in range(len(dp[i])):
            dp[i][j] = max(dp[i + 1][j], dp[i + 1][j + 1]) + m[i][j]

    print(dp[0][0])

    num -= 1
