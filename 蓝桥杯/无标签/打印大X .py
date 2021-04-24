m, n = map(int, input().strip().split())
kuan = m + 2*(n//2)
result = [['.' for _ in range(kuan)] for _ in range(n//2 + 1)]

for i in range(n//2+1):
    for j in range(i, i+m):
        result[i][j] = '*'
    for j in range(kuan-i-m, kuan-i):
        result[i][j] = '*'

for i in range(n//2-1, -1, -1):
    result.append(result[i])

for i in range(n):
    print(''.join(result[i]))
