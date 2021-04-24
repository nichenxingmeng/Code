n, k = map(int, input().strip().split())
xulie = list(map(int, input().strip().split()))
count = 0
a = [0 for _ in range(n)]
temp = [0 for _ in range(k)]

for S in range((1 << n) - 1, -1, -1):
    cnt = 0
    for i in range(n):
        if S & (1 << i):
            a[cnt] = i
            cnt += 1
    if cnt == k:
        for i in range(k-1, -1, -1):
            temp[i] = xulie[a[i]]
        flag = True
        for i in range(k-1):
            if temp[i+1] <= temp[i]:
                flag = False
                break
        if flag:
        count += 1
        count = count % 1000007
print(count % 1000007)
        
        










