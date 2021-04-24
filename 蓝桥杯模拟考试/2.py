from copy import deepcopy
n, m = map(int, input().strip().split())
tupian = []
walk = [[0,1],[0,-1],[1,0],[-1,0],[-1,-1],[-1,1],[1,1],[1,-1]]
result = [[0 for _ in range(m)] for _ in range(n)]

for i in range(n):
    tupian.append([int(j) for j in input().strip().split()])

for i in range(n):
    for j in range(m):
        if result[i][j] == 0:
            temp = []
            temp.append(tupian[i][j])
            for k in range(8):
                x = i + walk[k][0]
                y = j + walk[k][1]
                if x >= 0 and x < n and y >= 0 and y < m:
                    temp.append(tupian[x][y])
                    if tupian[x][y] == 255:
                        break
        result[i][j] = str(max(temp))

for i in range(n):
    print(' '.join(result[i]))
