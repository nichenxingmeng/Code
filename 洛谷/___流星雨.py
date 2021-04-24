m = int(input().strip())
liuxing = []
for i in range(m):
    liuxing.append(list(map(int, input().strip().split())))
ans = [[-1 for _ in range(301)] for _ in range(301)]
death = [[99999 for _ in range(301)] for _ in range(301)]
walk = [[1,0],[0,1],[-1,0],[0,-1]]
for i in range(m):
    temp = death[liuxing[i][1]][liuxing[i][0]]
    if temp == 99999:
        death[liuxing[i][1]][liuxing[i][0]] = liuxing[i][2]
    else:
        death[liuxing[i][1]][liuxing[i][0]] = min(liuxing[i][2], temp)
    for j in range(4):
        nowx = liuxing[i][1]+walk[j][0]
        nowy = liuxing[i][0]+walk[j][1]
        if nowx >= 0 and nowx <= 300 and nowy >= 0 and nowy <= 300:
            now = death[nowx][nowy]
            if now == 99999:
                death[nowx][nowy] = liuxing[i][2]
            else:
                death[nowx][nowy] = min(liuxing[i][2], now)

Q = []
Q.append([0, 0])
ans[0][0] = 0
Ans = 99999

while Q:
    u = Q[0]
    ux = u[0]
    uy = u[1]
    Q.pop(0)
    for i in range(4):
        x = ux + walk[i][0]
        y = uy + walk[i][1]
        if x < 0 or x > 300 or y < 0 or y > 300 or ans[x][y] != -1 or ans[ux][uy] >= death[x][y]-1:
            continue
        ans[x][y] = ans[ux][uy] + 1
        Q.append([x, y])
        
for i in range(301):
    for j in range(301):
        if death[i][j] > 1000 and ans[i][j] != -1:
            Ans = min(Ans, ans[i][j])
                
if Ans == 9999:
    print(-1)
else:
    print(Ans)
