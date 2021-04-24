from copy import deepcopy
t = [[0,1,0,1,0,0,0,0,0],
    [1,0,1,0,1,0,0,0,0],
    [0,1,0,0,0,1,0,0,0],
    [1,0,0,0,1,0,1,0,0],
    [0,1,0,1,0,1,0,1,0],
    [0,0,1,0,1,0,0,0,1],
    [0,0,0,1,0,0,0,1,0],
    [0,0,0,0,1,0,1,0,1],
    [0,0,0,0,0,1,0,1,0]]
deng = [0 for _ in range(9)]
kaiguan = [0 for _ in range(9)]

def dfs(u):
    global deng
    if u == 9:
        if sum(deng) == 4:
            for x in deng:
                print(x, end = '')
            print()
        return
    backup = deepcopy(deng)
    kaiguan[u] = 0
    dfs(u+1)
    deng = deepcopy(backup)
    kaiguan[u] = 1
    for i in range(9):
        deng[i] = deng[i]^t[u][i]
    dfs(u+1)

dfs(0)
