n, m = map(int, input().strip().split())
un = [_ for _ in range(n + 1)]

def find(x):
    if un[x] == x:
        return x
    un[x] = find(un[x])
    return un[x]

def join(x, y):
    f1 = find(x)
    f2 = find(y)
    if f1 != f2:
        un[f1] = f2

for i in range(m):
    x, y = map(int, input().strip().split())
    join(x, y)

ans = []
for i in range(1, n + 1):
    temp = find(i)
    if temp not in ans:
        ans.append(temp)

Len = len(ans)
if Len == 1:
    print('YES')
else:
    print('NO')
