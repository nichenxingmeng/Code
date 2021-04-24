n, m, p = map(int, input().strip().split())
fa = [_ for _ in range(n + 1)]

def find(x):
    if fa[x] == x:
        return x
    fa[x] = find(fa[x])
    return fa[x]

def join(x, y):
    f1 = find(x)
    f2 = find(y)
    if f1 != f2:
        fa[f1] = f2

for i in range(m):
    x, y = map(int, input().strip().split())
    join(x,y)

for i in range(p):
    x, y = map(int, input().strip().split())
    if find(x) == find(y):
        print('Yes')
    else:
        print('No')
