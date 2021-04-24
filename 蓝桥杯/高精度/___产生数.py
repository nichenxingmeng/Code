'''
from copy import deepcopy
temp = list(map(int, input().strip().split()))
m = []
n = list(str(temp[0]))
k = temp[1]
first = []

for i in range(k):
    temp_ = list(map(str, input().strip().split()))
    first.append(temp_[0])
    m.append(temp_)

count = 0
for i in range(k):
    if m[i][0] in n:
        count += 1

print(2**count)
'''
n, m = input().strip().split()
m = int(m)
bianhuan = [[0 for _ in range(10)] for _ in range(10)]
f = [0 for _ in range(10)]

for i in range(m):
    temp = list(map(int, input().strip().split()))
    bianhuan[temp[0]][temp[1]] = 1

for k in range(1, 10):
    for i in range(10):
        for j in range(1, 10):
            if bianhuan[i][k] == 1 and bianhuan[k][j] == 1:
                bianhuan[i][j] = 1

for i in range(10):
    bianhuan[i][i] = 1
    for j in range(10):
        if bianhuan[i][j] == 1:
            f[i] += 1

result = 1
temp_ = list(map(int, n))
for i in temp_:
    result *= f[i]
print(result)
