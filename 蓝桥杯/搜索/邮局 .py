'''
from math import sqrt
import sys
from itertools import permutations 
INF = sys.maxsize

def juli(x, y, x_, y_):
    return sqrt((x - x_) ** 2 + (y - y_) ** 2)

n, m, k = map(int, input().strip().split())
cunmin = []
youju = []
for i in range(n):
    x, y = map(int, input().strip().split())
    cunmin.append([x, y])
for i in range(m):
    x, y = map(int, input().strip().split())
    youju.append([x, y])

cnt = INF
ans = 0
tmp_ = list(permutations([i for i in range(1, m + 1)], k))
tmp = []
for i in range(len(tmp_)):
    tmp__ = list(tmp_[i])
    tmp__.sort()
    if tmp__ not in tmp:
        tmp.append(tmp__)

for i in range(len(tmp)):
    dist = 0
    for j in range(n):
        dist_ = INF
        for l in range(k):
            dist_ = min(dist_, juli(cunmin[j][0], cunmin[j][1], youju[tmp[i][l] - 1][0], youju[tmp[i][l] - 1][1]))
        dist += dist_
    if dist < cnt:
        ans = i
        cnt = dist

print(' '.join(map(str, tmp[ans])))
'''
from math import sqrt
import sys
from itertools import permutations 
INF = sys.maxsize
from copy import deepcopy

def juli(x, y, x_, y_):
    return sqrt((x - x_) ** 2 + (y - y_) ** 2)

def zhuanhuan(j, tmp):
    tmp_ = []
    for i in range(len(tmp)):
        tmp_.append(cunmin_[j].index(tmp[i]))
    return tmp_

n, m, k = map(int, input().strip().split())
cunmin = []
youju = []
for i in range(n):
    x, y = map(int, input().strip().split())
    cunmin.append([x, y])
for i in range(m):
    x, y = map(int, input().strip().split())
    youju.append([x, y])
    
cunmin_ = [[0 for _ in range(m)] for _ in range(n)]
cunmin__ = [[0 for _ in range(m)] for _ in range(n)]
for i in range(n):
    for j in range(m):
        cunmin_[i][j] = [j + 1, juli(cunmin[i][0], \
                        cunmin[i][1], youju[j][0], youju[j][1])]

    cunmin_[i].sort(key = lambda x : x[1])
    for j in range(m):
        cunmin__[i][j] = cunmin_[i][j][1]
        cunmin_[i][j] = cunmin_[i][j][0]

cnt = INF
ans = 0
tmp_ = list(permutations([i for i in range(1, m + 1)], k))
tmp = []
for i in range(len(tmp_)):
    tmp__ = list(tmp_[i])
    tmp__.sort()
    if tmp__ not in tmp:
        tmp.append(tmp__)

for i in range(len(tmp)):
    dist = 0
    for j in range(n):   
        dist += cunmin__[j][min(zhuanhuan(j, tmp[i]))]
    if dist < cnt:
        ans = i
        cnt = dist

print(' '.join(map(str, tmp[ans])))
