n = int(input().strip())
ID = []
for i in range(n):
    ID.append([int(j) for j in input().strip().split()])

m = [0 for _ in range(100001)]

for i in range(n):
    for j in range(len(ID[i])):
        if m[ID[i][j]] == 0:
            m[ID[i][j]] = 1
        else:
            b = ID[i][j]
start = m.index(1)
for i in range(start, 100001):
    if m[i] == 0:
        a = i
        break

print(a, b)
            
