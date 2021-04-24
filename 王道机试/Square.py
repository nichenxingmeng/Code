'''
import sys
n = list(map(int, input().strip().split()))
sum_ = sum(n) - n[0]

def dfs(n):
    global cnt, temp, temp_
    if cnt == 3:
        print('yes')
        sys.exit()
    for i in range(len(n)):
        if n[i] == 0:
            continue
        if n[i] >length:
            print('no')
            sys.exit()
        if n[i] == length:
            cnt += 1
            n[i] = 0
            dfs(n)
        if temp + n[i] < length:
            temp += n[i]
            temp__ = n[i]
            temp_.append(temp__)
            dfs(n)
            temp -= n[i]
            temp_.remove(temp__)
        elif temp + n[i] == length:
            temp += n[i]
            temp_.append(n[i])
            cnt += 1
            for i in range(len(temp_)):
                if temp_[i] in n:
                    n[n.index(temp_[i])] = 0
            temp = 0
            dfs(n)

if sum_ % 4 != 0:
    print('no')
else:
    length = sum_ // 4
    temp = 0
    cnt = 0
    temp_ = []
    n.pop(0)
    dfs(n)
'''
import sys
n = list(map(int, input().strip().split()))
sum_ = sum(n) - n[0]

def dfs(n):
    global cnt, temp, temp_
    if cnt == 3:
        print('yes')
        sys.exit()
    for i in range(len(n)):
        if n[i] == 0:
            continue
        if n[i] >length:
            print('no')
            sys.exit()
        if n[i] == length:
            cnt += 1
            n[i] = 0
            dfs(n)
        if temp + n[i] < length:
            temp += n[i]
            temp_.append(n[i])
            dfs(n)
            temp -= n[i]
            temp_.remove(n[i])
        elif temp + n[i] == length:
            temp += n[i]
            temp_.append(n[i])
            cnt += 1
            for i in range(len(temp_)):
                if temp_[i] in n:
                    n[n.index(temp_[i])] = 0
            temp = 0
            dfs(n)

if sum_ % 4 != 0:
    print('no')
else:
    length = sum_ // 4
    temp = 0
    cnt = 0
    temp_ = []
    n.pop(0)
    dfs(n)
