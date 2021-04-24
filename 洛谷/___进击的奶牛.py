n, c = map(int, input().strip().split())
a = [0 for _ in range(n+1)]
for i in range(1, n+1):
    a[i] = int(input().strip())
a.sort()

def P(x):
    k = 0
    last = -9999
    for i in range(1, n+1):
        if a[i] - last >= x:
            k += 1
            last = a[i]
    return k >= x

L = 0
R = 9999
while L <= R:
    mid = L + R >> 1
    if P(mid):
        ans = mid
        L = mid +1
    else:
        R = mid - 1
print(ans)
