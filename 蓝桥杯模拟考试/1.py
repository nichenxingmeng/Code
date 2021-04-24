from copy import deepcopy
n = int(input().strip())
wupin = []
for i in range(n):
    temp = [j for j in input().strip().split()]
    wupin.append([int(temp[0]), temp[1]])

min_ = 100001
shuxing = []
count = 0
flag = False

def dfs(i):
    global wupin, shuxing, min_, count, flag
    if i > n-1:
        return
    back = deepcopy(shuxing)
    back_ = count
    if len(wupin[i][1]) == 1:
        shuxing.append(wupin[i][1])
    elif len(wupin[i][1]) == 2:
        shuxing.append(wupin[i][1][0])
        shuxing.append(wupin[i][1][1])
    else:
        shuxing.append(wupin[i][1][0])
        shuxing.append(wupin[i][1][1])
        shuxing.append(wupin[i][1][2])
    count += wupin[i][0]
    if 'A' in shuxing and 'B' in shuxing and 'C' in shuxing:
        flag = True
        if count < min_:
            min_ = count
    dfs(i+1)
    count = back_
    shuxing = deepcopy(back)
    dfs(i+1)

dfs(0)

if not flag:
    print(-1)
else:
    print(min_)
