n = int(input().strip())
m = []
for i in range(n):
    m.append(list(map(int, input().strip().split())))

for i in range(n-1):
    a = m[i][0]
    b = m[i][1]
    temp = [[' ' for _ in range(a)] for _ in range(a-1)]
    for j in range(a-1):
        temp[j][j] = 'X'
        temp[j][a-j-1] = 'X'
    temp = temp*b
    for j in range(len(temp)):
        for k in range(a):
            print(temp[j][k], end = '')
        print()
    for j in range(a):
        print(temp[0][j], end = '')
    print()
    print()
i = n-1
a = m[i][0]
b = m[i][1]
temp = [[' ' for _ in range(a)] for _ in range(a-1)]
for j in range(a-1):
    temp[j][j] = 'X'
    temp[j][a-j-1] = 'X'
temp = temp*b
for j in range(len(temp)):
    for k in range(a):
        print(temp[j][k], end = '')
    print()
for j in range(a):
    print(temp[0][j], end = '')
print() 
