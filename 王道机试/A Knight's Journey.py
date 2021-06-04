n, m = map(int, input().strip().split()) 

qipan = [[0 for _ in range(m)] for _ in range(n)]
qipan[0][0] = 1

walk = [[-1,-2],[1,-2],[-2,-1],[2,-1],[-2,1],[2,1],[-1,2],[1,2]]

def dfs(x, y):
    global flag, Stack, ans
    if flag:
        return
    tmp = 0
    for i in range(n):
        tmp += sum(qipan[i])
    if tmp == n * m:
        flag = True
        ans_ = []
        for i in range(len(Stack)):
            ans_.append(chr(ord('A') + Stack[i][0]))
            ans_.append(Stack[i][1] + 1)
        ans.append(ans_)
        return
    for i in range(8):
        x_ = x + walk[i][0]
        y_ = y + walk[i][1]
        if x_ >= 0 and x_ < n and y_ >= 0 and y_ < m and qipan[x_][y_] == 0:
            qipan[x_][y_] = 1
            Stack.append([x_, y_])
            dfs(x_, y_)
            qipan[x_][y_] = 0
            Stack.remove([x_, y_])
                    
flag = False
Stack = [[0, 0]]
ans = []
dfs(0, 0)
if not flag:
    print('impossible')
else:
    print(''.join(map(str, ans[0])))
