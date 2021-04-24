n, m = map(int, input().strip().split())
a = []
for i in range(n):
    a.append([int(j) for j in input().strip().split()])
b = []
for i in range(n):
    b.append([int(j) for j in input().strip().split()])

ans = [[0 for _ in range(m)] for _ in range(n)]
for i in range(n):
    for j in range(m):
        ans[i][j] += a[i][j]
        ans[i][j] += b[i][j]

for i in range(n):
    print(' '.join(map(str, ans[i])))
