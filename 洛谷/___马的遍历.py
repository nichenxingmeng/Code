Q = []
n, m, sx, sy = map(int, input().strip().split())
ans = [[-1 for _ in range(m+1)] for _ in range(n+1)]
walk = [[2,1],[1,2],[-1,2],[-2,1],[-2,-1],[-1,-2],[1,-2],[2,-1]]
temp = [sx, sy]
ans[sx][sy] = 0
Q.append(temp)

while Q:
    u = Q[0]
    ux = u[0]
    uy = u[1]
    Q.pop(0)
    for k in range(8):
        d = ans[ux][uy]
        x = ux + walk[k][0]
        y = uy + walk[k][1]
        if x < 1 or x > n or y < 1 or y > m or ans[x][y] != -1:
            continue
        ans[x][y] = d + 1
        temp = [x,y]
        Q.append(temp)

for i in range(1, n+1):
    for j in range(1, m+1):
        print(ans[i][j], end = ' ')
    print()

            
