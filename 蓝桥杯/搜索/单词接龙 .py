from copy import deepcopy
n = int(input().strip())
danci = []
for i in range(n):
    danci.append(input().strip())
danci_num = [2 for _ in range(n)]
start = input().strip()
temp = []
ans = 0
count = 0

def dfs(x):
    global danci_num, danci, ans, flag, temp, count
    for i in range(n):
        if danci[i][0] == x and danci_num[i] != 0:
            flag = True
            temp.append(danci[i][1:])
            danci_num[i] -= 1
            dfs(danci[i][-1])
            dfs(danci[i][len(danci[i])-2:])
            temp.remove(danci[i][1:])
            flag = False
            danci_num[i] += 1
        if danci[i][0:2] == x and danci_num[i] != 0 and len(danci[i]) > 2:
            flag = True
            temp.append(danci[i][2:])
            danci_num[i] -= 1
            dfs(danci[i][-1])
            dfs(danci[i][len(danci[i])-2:])
            temp.remove(danci[i][2:])
            flag = False
            danci_num[i] += 1
    if flag:
        for i in range(len(temp)):
            count += len(temp[i])
        if count > ans:
            ans = count
        count = 0
    return

flag = False
dfs(start)
print(ans + len(start))
