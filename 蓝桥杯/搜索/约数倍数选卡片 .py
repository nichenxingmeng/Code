import sys
INF = sys.maxsize

kapai = list(map(int, input().strip().split()))
xuanze = list(map(int, input().strip().split()))

def yueshu(x, now):
    if x % now == 0:
        return True
    return False

def beishu(x, now):
    if now % x == 0:
        return True
    return False

MIN = INF

def dfs(x, n, s):
    global kapai, ans
    flag = False
    tmp = []
    
    for i in range(len(kapai)):
        if beishu(x, kapai[i]) or yueshu(x, kapai[i]):
            tmp.append(kapai[i])
            flag = True
    if not flag or kapai == []:
        if n & 1:
            cnt[s] += 1
        else:
            cnt[s] -= 1
        return
    
    for i in range(len(tmp)):
        temp = tmp[i]
        kapai.remove(temp)
        ans.append(temp)
        dfs(temp, n + 1, s)
        kapai.append(temp)
        ans.remove(temp)
    
ans = []
cnt = [0 for _ in range(len(xuanze))]
back = kapai
back_ = ans
for i in range(len(xuanze)):
    kapai = back
    ans = back_
    temp = xuanze[i]
    kapai.remove(temp)
    ans.append(temp)
    dfs(temp, 0, i)
    kapai.append(temp)
    ans.remove(temp)

for i in range(len(xuanze)):
    if cnt[i] > 0:
        MIN = min(MIN, xuanze[i])

if MIN == INF:
    print('-1')
else:
    print(MIN)
