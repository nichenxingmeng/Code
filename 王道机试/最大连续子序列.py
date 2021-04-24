k = int(input().strip())
m = list(map(int, input().strip().split()))
dp = [0 for _ in range(k)]
dp[0] = m[0]
temp = [[] for _ in range(k)]

start = 0
for i in range(1, k):
    dp[i] = max(m[i], dp[i-1]+m[i])

ans = max(dp)
print(ans)
end = dp.index(ans)
cnt = 0
for i in range(end, -1, -1):
    cnt += m[i]
    if cnt == ans:
        start = i
        break
print(m[start])
print(m[end])
