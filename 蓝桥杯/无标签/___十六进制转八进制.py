n = int(input())
m = []
for i in range(n):
    m.append(str(input()))
for i in range(n):
    m[i] = int(m[i], 16)
    m[i] = oct(m[i])
    print(m[i][2:])
