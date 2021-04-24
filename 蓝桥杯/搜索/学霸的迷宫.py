n, m = map(int, input().strip().split())
migong = []
for i in range(n):
    migong.append([int(i) for i in input()])
ans = [[-1 for _ in range(m)] for _ in range(n)]
ans[0][0] = 0
guiji = [[-1 for _ in range(m)] for _ in range(n)]
Q = []
Q.append([0, 0])
fangxiang = ['D', 'L', 'R', 'U']
walk = [[1,0],[0,-1],[0,1],[-1,0]]
guanxi = [[[-2, -2] for _ in range(m)] for _ in range(n)]

while Q:
    u = Q[0]
    Q.pop(0)
    ux = u[0]
    uy = u[1]
    for i in range(4):
        d = ans[ux][uy]
        x = ux + walk[i][0]
        y = uy + walk[i][1]
        if x < 0 or x > n-1 or y < 0 or y > m-1 or migong[x][y] == 1 \
               or ans[x][y] != -1:
            continue
        ans[x][y] = d + 1
        guiji[x][y] = i
        guanxi[x][y][0] = [ux, uy]
        guanxi[ux][uy][1] = [x, y]
        Q.append([x, y])
        
print(ans[n-1][m-1])
result = []
i = n - 1
j = m - 1
while guanxi[i][j][0] != -2:
    result.append(guiji[i][j])
    i, j = guanxi[i][j][0][0], guanxi[i][j][0][1]
result = result[::-1]
for i in range(len(result)):
    print(fangxiang[result[i]], end = '')
