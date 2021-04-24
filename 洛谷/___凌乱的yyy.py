n = int(input().strip())
m = []
for i in range(n):
    m.append(list(map(float, input().strip().split())))

m.sort(key = lambda x: x[1])

ans = 0
finish = m[0][1]
for i in range(1, n):
    if m[i][0] >= finish:
        ans += 1
        finish = m[i][1]
print(ans)
