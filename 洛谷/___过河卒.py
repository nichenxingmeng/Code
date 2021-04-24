n, m, hx, hy = map(int, input().strip().split())

d = [[0,0],[1,2],[1,-2],[-1,2],[-1,-2],[2,1],[2,-1],[-2,1],[-2,-1]]
ctrl = [[0 for _ in range(22)] for _ in range(22)]
f = [[0 for _ in range(22)] for _ in range(22)]

for i in range(9):
    tempx = hx + d[i][0]
    tempy = hx + d[i][1]
    if tempx >= 0 and tempx <= n and tempy >= 0 and tempy <= m:
        ctrl[tempx][tempy] = 1
f[0][0] = 1 - ctrl[0][0]
for i in range(n+1):
    for j in range(m+1):
        if ctrl[i][j]:
            continue
        if i != 0:
            f[i][j] += f[i-1][j]
        if j != 0:
            f[i][j] += f[i][j-1]
print(f[n][m])
