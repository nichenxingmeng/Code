def First(a):
    return a[0]

def check(m, n):
    m *= 2
    j = 0
    for i in range(n):
        while j < n and a[j][0] - a[i][0] <= m:
            j += 1
        Max = -1e10
        Min = 1e10
        if j!= n:
            Max = max(Max, fr[j][1])
            Min = min(Min, fr[j][0])
        if i - 1 >= 0:
            Max = max(Max, fL[i-1][1])
            Min = min(Min, fL[i-1][0])
        if Max - Min <= m:
            return True
    return False

n = int(input())
a = []
for i in range(n):
    a.append(list(map(int, input().strip().split())))
for i in range(n):
    a[i][0], a[i][1] = a[i][0]+a[i][1], a[i][0]-a[i][1]
a.sort(key = First)

fL = [[[], []] for x in range(len(a))]
fr = [[[], []] for x in range(len(a))]
fL[0][0] = a[0][1]
fL[0][1] = a[0][1]
for i in range(1, n):
    fL[i][1] = max(fL[i-1][1], a[i][1])
    fL[i][0] = min(fL[i-1][0], a[i][1])
fr[n-1][0] = a[n-1][1]
fr[n-1][1] = a[n-1][1]
for i in range(n-2, 0, -1):
    fr[i][1] = max(fr[i+1][1], a[i][1])
    fr[i][0] = min(fr[i+1][0], a[i][1])

L = 0.0
r = 1000000000
while r-L >= 0.01:
    m = (L+r)/2
    if check(m, n):
        r = m
    else:
        L = m
print('{:.1f}'.format(r))
