n = int(input().strip())
leiqu = []
for i in range(n):
    shuru = [str(j) for j in input().strip().split()]
    if 'A' in shuru:
        A = [i, shuru.index('A')]
    if 'B' in shuru:
        B = [i, shuru.index('B')]
    leiqu.append(shuru)
guiji = [[-1 for _ in range(5)] for _ in range(5)]
walk = [[0,1],[0,-1],[1,0],[-1,0]]
Q = []
Q.append([A[0], A[1]])
guiji[A[0]][A[1]] = 0

while Q:
    u = Q[0]
    ux = u[0]
    uy = u[1]
    Q.pop(0)
    for i in range(4):
        x = ux + walk[i][0]
        y = uy + walk[i][1]
        d = guiji[ux][uy]
        if x < 0 or x > n-1 or y < 0 or y > n-1 or guiji[x][y] != -1 \
               or leiqu[x][y] == leiqu[ux][uy]:
            continue
        guiji[x][y] = d + 1
        Q.append([x, y])

print(guiji[B[0]][B[1]])
