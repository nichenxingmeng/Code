n, m = map(int, input().strip().split())
juzhen = []
for i in range(n):
    juzhen.append([int(j) for j in input().strip().split()])

result = [[0 for _ in range(n)] for _ in range(m)]

for i in range(n):
    for j in range(m):
        result[j][i] = str(juzhen[i][j])
for i in range(m):
    print(' '.join(result[i]))
