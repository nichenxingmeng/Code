from copy import deepcopy
n, m = map(int, input().split())
a = [[] for x in range(n)]
b = [[] for x in range(n)]
c = [[[] for x in range(n)] for x in range(n)]

for i in range(n):
    a[i] = list(map(int,input().split()))

b = deepcopy(a)

def chengfa(a, n, m):
    global b, c
    if m >= 2:
        for i in range(n):
            for j in range(n):
                cnt = 0
                for k in range(n):
                    cnt += b[i][k] * a[k][j]
                c[i][j] = cnt
                
        b = deepcopy(c)
        chengfa(a, n, m - 1)

if m == 0:
    for i in range(n):
        for j in range(n):
            if i == j:
                c[i][j] = 1
            else:
                c[i][j] = 0
else:
    chengfa(a, n, m)

for i in range(n):
    for j in range(n):
        print(c[i][j], end=' ')
    print('')
