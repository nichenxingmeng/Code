from copy import deepcopy
n = int(input().strip())
north = [int(i) for i in input().strip().split()]
west = [int(i) for i in input().strip().split()]

chengbao = [[0 for _ in range(n)] for _ in range(n)]
chengbao[0][0] = 0
walk = [[1,0], [-1,0], [0,1], [0,-1]]
ans = [[0 for _ in range(n)] for _ in range(n)]
ans[0][0] = 1
guanxi = [[[-2, -2] for _ in range(n)] for _ in range(n)]
guanxi_ = []

def man(ans):
    global west, north
    flag1 = False
    flag2 = False
    for i in range(n):
        if sum(ans[i]) != west[i]:
            flag1 = True
            break
    for i in range(n):
        sum_ = 0
        for j in range(n):
            sum_ += ans[j][i]
        if sum_ != north[i]:
            flag2 = True
            break
    if not flag1 and not flag2:
        return True
    else:
        return False

def dfs(ux, uy):
    if ux == n-1 and uy == n-1 and man(ans):
        start = guanxi[n-1][n-1]
        while start[0] != -2:
            guanxi_.append(start[0])
            start = guanxi[start[0][0]][start[0][1]]
        return
    for i in range(4):
        x = ux + walk[i][0]
        y = uy + walk[i][1]
        d = chengbao[ux][uy]
        if x >= 0 and x < n and y >= 0 and y < n and ans[x][y] == 0 and \
                sum(ans[x]) < west[x]:    
            sum_ = 0
            for j in range(n):
                sum_ += ans[j][y]
            if sum_ < north[y]:
                back = chengbao[x][y]
                ans[x][y] = 1
                chengbao[x][y] = d + 1
                guanxi[x][y][0] = [ux, uy]
                guanxi[ux][uy][1] = [x, y]
                dfs(x, y)
                chengbao[x][y] = back
                ans[x][y] = 0

dfs(0, 0)
guanxi_ = guanxi_[::-1]
result = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        result[i][j] = i*n+j
    
for i in range(len(guanxi_)):
    print(result[guanxi_[i][0]][guanxi_[i][1]], end = ' ')
print(n*n-1)
