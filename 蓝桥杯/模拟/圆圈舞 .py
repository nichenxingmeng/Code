from copy import deepcopy

n = int(input().strip())
dongwu = []
for i in range(n):
    Hi, Fi = map(int, input().strip().split())
    dongwu.append([Hi, Fi])
dongwu.insert(0, [])
m = int(input().strip())
duiwu = [[i + 1 for i in range(10)]]

for _ in range(m):
    k, p, q = map(int, input().strip().split())
    if k == 2:
        dongwu[p][0] = q
    elif k == 3:
        dongwu[p][1] = q 
    elif k == 1:
        flag1 = False
        flag2 = False
        for i in range(len(duiwu)):
            if p in duiwu[i]:
                p_index = i
                flag1 = True
            if q in duiwu[i]:
                q_index = i
                flag2 = True
            if flag1 and flag2:
                break
        p_index_ = duiwu[p_index].index(p)
        q_index_ = duiwu[q_index].index(q)
        if p_index == q_index:
            if p_index_ - q_index_ == -1 or (p_index_ == len(duiwu[p_index]) \
                and q_index_ == 0):
                ans = 0
                for i in range(len(duiwu)):
                    t = len(duiwu[i])
                    for j in range(t):
                        for L in range(1, t):
                            you = (j + L) % t
                            ans += (t-L)*dongwu[duiwu[i][j]][0]*dongwu[duiwu[i][you]][1]
                            ans %= 1000000007
                print(ans)
                continue
            if p_index_ < q_index_:
                tmp = deepcopy(duiwu[p_index])
                duiwu[p_index] = []
                for j in range(p_index_ + 1):
                    duiwu[p_index].append(tmp[j])
                for j in range(q_index_, len(tmp)):
                    duiwu[p_index].append(tmp[j])
                tmp_ = []
                for j in range(p_index_ + 1, q_index_):
                    tmp_.append(tmp[j])
                duiwu.append(tmp_) 
            else:
                tmp = deepcopy(duiwu[p_index])
                duiwu[p_index] = []
                for j in range(q_index_):
                    duiwu[p_index].append(tmp[j])
                for j in range(p_index_ + 1, len(tmp)):
                    duiwu[p_index].append(tmp[j])
                tmp_ = []
                for j in range(q_index_, p_index_ + 1):
                    tmp_.append(tmp[j])
                duiwu.append(tmp_)
        else:
            tmp = deepcopy(duiwu[q_index])
            tmp_ = deepcopy(tmp[q_index_:])
            tmp = deepcopy(tmp[:q_index_])
            for i in range(len(tmp)):
                tmp_.append(tmp[i])
            for i in range(len(tmp_)):
                duiwu[p_index].insert(p_index_ + i + 1, tmp_[i])
            duiwu.pop(q_index)

    ans = 0
    for i in range(len(duiwu)):
        t = len(duiwu[i])
        for j in range(t):
            for L in range(1, t):
                you = (j + L) % t
                ans += (t-L)*dongwu[duiwu[i][j]][0]*dongwu[duiwu[i][you]][1]
                ans %= 1000000007
    print(ans % 1000000007)
            
