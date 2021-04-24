from copy import deepcopy
from itertools import permutations
n = int(input().strip())
m = []
for i in range(n):
    m.append(list(map(int, input().strip().split())))
for i in range(n):
    m[i].append(0)
temp = deepcopy(m)

for k in range(n):
    pailie = list(permutations([x for x in range(1, m[k][0]+1)]))
    m = deepcopy(temp)
    for j in pailie:
        alist = list(j)
        exchange = True
        count = 0
        passnum = n-1
        while passnum > 0 and exchange:
            exchange = False
            for i in range(passnum):
                if alist[i] > alist[i+1]:
                    exchange = True
                    alist[i], alist[i+1] = alist[i+1], alist[i]
            if exchange:
                count += 1
            passnum -= 1
        m[count][2] += 1
            
for i in range(len(m)):
    print(m[i][2]%20100713)
