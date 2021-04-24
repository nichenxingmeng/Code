from copy import deepcopy
n = int(input().strip())
qipan = []
for i in range(n):
    qipan.append([int(j) for j in input().strip().split()])
qipan_ = deepcopy(qipan)

def dfs(x, m):
    global ans, temp, qipan, qipan_

    if x > m - 1:
        ans += 1
        #print(temp)
        return
    for i in range(n):
        for j in range(n):
            if qipan[i][j] != 0:
                back = deepcopy(qipan)
                for i_ in range(i-1, -1, -1):
                    if qipan_[i_][j] == 1:
                        qipan[i_][j] = 0
                    else:
                        break
                for i__ in range(i, n, 1):
                    if qipan_[i__][j] == 1:
                        qipan[i__][j] = 0
                    else:
                        break
                for j_ in range(j-1, -1, -1):
                    if qipan_[i][j_] == 1:
                        qipan[i][j_] = 0
                    else:
                        break
                for j__ in range(j+1, n, 1):
                    if qipan_[i][j__] == 1:
                        qipan[i][j__] = 0
                    else:
                        break
                temp.append([i, j])
                dfs(x+1, m)
                qipan = deepcopy(back)
                temp.remove([i, j])
        
def jiecheng(x):
    if x == 1:
        return 1
    else:
        return x*jiecheng(x-1)

for i in range(10000):
    ans = 0
    temp = []
    dfs(0, i+1)
    if ans != 0:
        print(ans // jiecheng(i+1))
    else:
        break
