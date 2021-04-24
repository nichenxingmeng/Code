import sys
sys.setrecursionlimit(1000000)
from copy import deepcopy
d = list(map(int, input().strip().split()))
a = list(map(int, input().strip().split()))
b = list(map(int, input().strip().split()))
c = list(map(int, input().strip().split()))

def panduan(n):
    global a, b, c
    global count
    global temp_d
    temp_d[0] -= n[0]
    temp_d[1] -= n[1]
    temp_d[2] -= n[2]
    if n == a:
        count[0] += 1
    if n == b:
        count[1] += 1
    if n == c:
        count[2] += 1

def dfs():
    global flag
    global temp_d
    global count
    if not flag:
        if temp_d[0] == 0 and temp_d[1] == 0 and temp_d[2] == 0:
            print(count[0],count[1],count[2],(count[0]*a[0]+count[1]*b[0] \
                      +count[2]*c[0])//d[0] ,sep=' ')
            flag = True
            return
        elif temp_d[0] >= 0 and temp_d[1] >= 0 and temp_d[2] >= 0:
            backup_ = deepcopy(count)
            backup = deepcopy(temp_d)
            panduan(a)
            dfs()
            count = deepcopy(backup_)
            temp_d = deepcopy(backup)
            backup = deepcopy(temp_d)
            backup_ = deepcopy(count)
            panduan(b)
            dfs()
            temp_d = deepcopy(backup)
            count = deepcopy(backup_)
            panduan(c)
            dfs()
        else:
            return
    else:
        return
        

for i in range(1, 1000):
    temp_d = [d[0]*i, d[1]*i, d[2]*i]
    count = [0, 0, 0]
    flag = False
    dfs()
    if flag:
        break
if not flag:
    print('NONE')

