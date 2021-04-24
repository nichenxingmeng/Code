'''
n, k = map(int, input().strip().split())
shu = list(map(int, input().strip().split()))
a = [0 for _ in range(n)]
shu.sort()

for S in range(1 << n):
    cnt = 0
    for i in range(n):
        if S & (1 << i):
            a[cnt] = i
            cnt += 1
    if cnt == 3:
        count = 0
        for i in range(3):
            count += shu[n - a[i] - 1]
        if count % k == 0:
            print(count)
            break
'''
'''
n, k = map(int, input().strip().split())
shu = list(map(int, input().strip().split()))
a = [0 for _ in range(n)]
max_ = 0

for S in range(1 << n):
    print(S)
    cnt = 0
    for i in range(n):
        if S & (1 << i):
            a[cnt] = i
            cnt += 1
    if cnt == 3:
        count = 0
        for i in range(3):
            count += shu[a[i]]
        if count % k == 0:
            if count > max_:
                max_ = count
print(max_)
'''

    
n, k = map(int, input().strip().split())
group = [[0 for _ in range(3)] for _ in range(1000)]
shu = list(map(int, input().strip().split()))
ans = 0

for i in range(n):
    x = shu[i]
    re = x % k

    if x > group[re][0]:
        group[re][2] = group[re][1]
        group[re][1] = group[re][0]
        group[re][0] = x
    elif x > group[re][1]:
        group[re][2] = group[re][1]
        group[re][1] = x
    elif x > group[re][2]:
        group[re][2] = x

for i in range(k):
    v1 = group[i][0]
    if v1 != 0:
        for j in range(i, k):
            if i == j:
                v2 = group[j][1]
            else:
                v2 = group[j][0]

            if v2 != 0:
                z = (k-(i+j)%k)%k
                if i != j:
                    if z != j and z != i:
                        v3 = group[z][0]
                    elif z == j:
                        v3 = group[j][1]
                    elif z == i:
                        v3 = group[i][1]
                else:
                    if z == i:
                        v3 = group[z][2]
                    else:
                        v3 = group[z][0]
                if v3 != 0:
                    ans = max(ans, v1 + v2 + v3)
                    
print(ans)
