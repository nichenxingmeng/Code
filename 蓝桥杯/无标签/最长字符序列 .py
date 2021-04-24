a, b = map(str, input().strip().split())

n = len(a)
max_ = -1

for S in range((1<<n)):
    cnt = []
    for i in range(n):
        if S&(1<<i):
            cnt.append(i)
    temp = ''
    for i in range(len(cnt)):
        temp += a[cnt[i]]
    if temp in b:
        if len(temp) > max_:
            max_ = len(temp)

print(max_)
