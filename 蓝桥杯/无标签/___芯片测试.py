n = int(input())
m = []
for i in range(n):
    m.append(list(map(int, input().split())))
for j in range(n):
    count = 0
    for i in range(n):
        if m[i][j] == 1:
            count += 1
    if count > n/2:
        print(j+1, end=' ')
