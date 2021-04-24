from copy import deepcopy
n, m = map(int, input().strip().split())
tongdao = []
zhan = set()
for i in range(m):
    shuru = list(map(int, input().strip().split()))
    tongdao.append(shuru)
    shuru_ = [shuru[1], shuru[0]]
    zhan.add(shuru[0])
    zhan.add(shuru[1])
    tongdao.append(shuru_)

u, v = map(int, input().strip().split())
zhan = list(zhan)
zhan.remove(u)
zhan.remove(v)

def dfs(temp, u, v):
    global count, flag, result
    for i in range(len(temp)): 
        if temp[i][0] == u:
            if temp[i][1] == v or temp[i][1] in result or temp[i][0] in result:
                flag = True
                result.append(u)
                return
            back = u
            back_ = deepcopy(temp[i])
            index_ = temp.index([temp[i][1], temp[i][0]])
            u = temp[i][1]
            temp[i] = [0, 0]
            temp[index_] = [0, 0]
            dfs(temp, u, v)
            u = back
            temp[i] = deepcopy(back_)
            temp[index_] = [back_[1], back_[0]]
    return
    
count = 0
for i in range(len(zhan)):
    result = []
    temp = deepcopy(tongdao)
    j = 0
    while j < len(temp):
        if temp[j][0] == zhan[i] or temp[j][1] == zhan[i]:
            temp.remove(temp[j])
            j -= 1
        j += 1
    flag = False
    dfs(temp, u, v)
    if not flag:
        count += 1
    #print(i)
print(count)
