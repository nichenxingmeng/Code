C = int(input().strip())
while C > 0:
    m, n = map(int, input().strip().split())
    v = [0 for _ in range(n)]
    w = [0 for _ in range(n)]
    k = [0 for _ in range(n)]
    weight = [0 for _ in range(m)]
    value = [0 for _ in range(m)]
    num = 0
    
    for i in range(n):
        w[i], v[i], k[i] = map(int, input().strip().split())
        j = 1
        while j <= k[i]:
            weight[num] = j * w[i]
            value[num] = j * v[i]
            k[i] -= j
            j <<= 1
            num += 1
            
        if k[i] > 0:
            weight[num] = k[i] * w[i]
            value[num] = k[i] * v[i]
            num += 1

    dp = [0 for _ in range(m + 1)]
    for i in range(num):
        for j in range(m, weight[i] - 1, -1):
            dp[j] = max(dp[j], dp[j - weight[i]] + value[i])
    print(dp[m])

    C -= 1
