'''
from copy import deepcopy
n = int(input().strip())
shujulian = []
for i in range(n):
    shuru = [int(j) for j in input().strip().split()]
    shuru_ = [shuru[1], shuru[0]]
    shujulian.append(shuru)
    shujulian.append(shuru_)

def dfs(x):
    global temp_
    global temp

    if x in temp:
        index_ = temp.index(x)
        temp_ = deepcopy(temp[index_:])
        return
    for i in range(len(shujulian)):
        if shujulian[i][0] == x:
            temp.append(x)
            back = deepcopy(shujulian[i])
            index = shujulian.index([shujulian[i][1],x])
            back_ = deepcopy(shujulian[index])
            shujulian[i] = [-1, -1]
            shujulian[index] = [-1, -1]
            dfs(back[1])
            temp.remove(x)
            shujulian[i] = deepcopy(back)
            shujulian[index] = deepcopy(back_)

for j in range(1, n+1):
    temp = []
    temp_ = []
    dfs(j)
    temp_.sort()
    if temp_:
        print(' '.join(map(str, temp_)))
        break
'''
from copy import deepcopy
n = int(input().strip())
shujulian = []
for i in range(n):
    shuru = [int(j) for j in input().strip().split()]
    shuru_ = [shuru[1], shuru[0]]
    shujulian.append(shuru)
    shujulian.append(shuru_)

def dfs(x):
    global temp_
    global temp

    if x in temp:
        index_ = temp.index(x)
        temp_ = deepcopy(temp[index_:])
        return
    index__ = shujilian.index([x, *])
    for i in range(len(shujulian)):
        if shujulian[i][0] == x:
            temp.append(x)
            back = deepcopy(shujulian[i])
            index = shujulian.index([shujulian[i][1],x])
            back_ = deepcopy(shujulian[index])
            shujulian[i] = [-1, -1]
            shujulian[index] = [-1, -1]
            dfs(back[1])
            temp.remove(x)
            shujulian[i] = deepcopy(back)
            shujulian[index] = deepcopy(back_)

for j in range(1, n+1):
    temp = []
    temp_ = []
    dfs(j)
    temp_.sort()
    if temp_:
        print(' '.join(map(str, temp_)))
        break
