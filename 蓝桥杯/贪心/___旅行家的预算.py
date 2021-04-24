import sys
D1, C, D2, P, N = map(float, input().strip().split())
N = int(N)
dis = C * D2
a = [0 for _ in range(N+1)]
for i in range(1, N+1):
    a[i] = list(map(float, input().strip().split()))
a[0] = [0]

for i in range(1, N+1):
    if a[i][0] - a[i-1][0] > dis:
        print('No Solution')
        sys.exit()

loc = 0
ca = 0
cost = 0
i = 0

while loc < D1:
    flag = False
    reach = loc + dis
    j = i + 1
    while j <= N and a[j][0] <= reach:
        if a[j][1] < P:
            flag = True
            t = j
            break
        j += 1
        
    if not flag:
        if reach >= D1:
            if (D1 - loc) / D2 > ca:
                cost += ((D1 - loc) / D2 - ca) * P
            break
        t = i + 1
        cost += (C - ca) * P
        ca = C - (a[t][0] - loc) / D2
        loc = a[t][0]
        p = a[t][1]
        i = t
    else:
        if (a[t][0] - loc) / D2 > ca:
            cost += ((a[t][0] - loc) / D2 - ca) * P
            ca = 0
        else:
            ca -= (a[t][0] - loc) / D2
        loc = a[t][0]
        P = a[t][1]
        i = t

print('{:.2f}'.format(cost))
