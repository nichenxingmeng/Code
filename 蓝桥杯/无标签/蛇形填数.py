n = int(input())
m = [[[]for x in range(n)] for x in range(n)]
count = 1
def zhuanquan(n, i, j):
    global m
    global count
    if count <= n*n:
        for x in range(i, n-i):
            m[x][n-j-1] = count
            count += 1
        for x in range(n-j-2,j-1,-1):
            m[n-i-1][x] = count
            count += 1
        for x in range(n-i-2,i-1,-1):
            m[x][j] = count
            count += 1
        for x in range(j+1, n-j-1):
            m[i][x] = count
            count += 1
        zhuanquan(n, i+1, j+1)
    else:
        return
zhuanquan(n, 0, 0)
print(m)
