m = []
for i in range(10):
    m.append(input().strip().split())

a = 0
b = 0
for i in range(10):
    a += int(m[i][0])
    b += int(m[i][1])
print(f'{a}+{b}i')
