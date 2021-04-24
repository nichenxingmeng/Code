C = int(input().strip())
while C > 0:
    e, f = map(int, input().strip().split())
    m = f - e
    n = int(input().strip())
    v = [0 for _ in range(n)]
    w = [0 for _ in range(n)]
    for i in range(n):
        v[i], w[i] = map(int, input().strip().split())
    dp = [10000 for _ in range(m + 1)]
    dp[0] = 0

    for i in range(n):
        for j in range(w[i], m + 1):
            dp[j] = min(dp[j], dp[j - w[i]] + v[i])
    
    if dp[m] == 10000:
        print('No')
    else:
        print(dp[m])
    
    C -= 1
