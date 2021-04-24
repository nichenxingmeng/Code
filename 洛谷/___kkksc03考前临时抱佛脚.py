m = [0 for _ in range(21)]

def dfs(x):
    global nowtime, maxtime
    if x > maxdeep:
        maxtime = max(maxtime, nowtime)
        return
    if nowtime + m[x] <= sum_ // 2:
        nowtime += m[x]
        dfs(x + 1)
        nowtime -= m[x]
    dfs(x + 1)

ans = 0
s = list(map(int, input().strip().split()))
for i in range(4):
    nowtime = 0
    maxtime = 0
    maxdeep = s[i]
    sum_ = 0
    for j in range(maxdeep + 1):
        m[j] = int(input().strip())
        sum_ += m[j]
    dfs(1)
    ans += sum_ - maxtime

print(ans)
    
