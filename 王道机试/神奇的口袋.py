
n = int(input().strip())
wupin = []
for i in range(n):
    wupin.append(int(input().strip()))

def dfs():
    global cnt, ans, temp, temp_
    if cnt == 40:
        temp.sort()
        if temp not in temp_:
            ans += 1
            temp_.append(temp[:])
        return
    for i in range(n):
        if wupin[i] == 0:
            continue
        if cnt + wupin[i] <= 40:
            cnt += wupin[i]
            back = wupin[i]
            wupin[i] = 0
            temp.append(i)
            dfs()
            wupin[i] = back
            cnt -= wupin[i]
            temp.remove(i)
        else:
            continue

cnt = 0
ans = 0
temp = []
temp_ = []
dfs()
print(ans)
