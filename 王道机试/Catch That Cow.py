xian = [-1 for _ in range(100001)]
n, k = map(int, input().strip().split())
xian[n] = 0

Q = []
Q.append(n)

while Q:
    u = Q[0]
    Q.pop(0)
    if u == k:
        print(xian[u])
        break
    for i in range(3):
        if i == 0:
            x = u - 1
        elif i == 1:
            x = u + 1
        elif i == 2:
            x = 2 * u
        if xian[x] != -1 or x > 100000:
            continue
        else:
            Q.append(x)
            xian[x] = xian[u] + 1
