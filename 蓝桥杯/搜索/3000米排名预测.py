from copy import deepcopy
from itertools import permutations
n, m = map(int, input().strip().split())
a = []
for i in range(m):
    a.append(list(map(int, input().strip().split())))
c = list(permutations([i for i in range(n)]))

for i in range(len(c)):
    flag = False
    flag0 = False
    for j in range(m):
        d = deepcopy(a[j][1:len(a[j])-1])
        e = deepcopy(c[i])
        if a[j][-1] == 0:
            for k in range(a[j][0]):
                for v in range(k+1, a[j][0]):
                    if e.index(d[k]) > e.index(d[v]):
                        flag0 = True
                        break
        if a[j][-1] == 1:
            for k in range(a[j][0]):
                for v in range(k+1, a[j][0]):
                    if  e.index(d[k]) > e.index(d[v]):
                        flag = True
                        break
    if flag == True or flag0 == False:
        c[i] = []
while [] in c:
    c.remove([])

print(len(c))
for i in range(len(c)):
    for j in range(n):
        print(c[i][j], end=' ')
    print('')
