a = list(map(float, input().split()))
b = list(map(float, input().split()))
amax = max(a[0], a[2])
amin = min(a[0], a[2])
bmax = max(b[0], b[2])
bmin = min(b[0], b[2])
if (a[0] > a[2] and a[1] < a[3]) or (a[0] < a[2] and a[1] > a[3]):
    a[1], a[3] = a[3], a[1]
    b[1], b[3] = b[3], b[1]
if amax >= bmax:
    s = (min(bmax, amax)-max(amin, bmin))*(min(b[b.index(bmax)+1], a[a.index(amax)+1])-max(a[a.index(amin)+1], b[b.index(bmin)+1]))
else:
    s = (min(amax, bmax)-max(bmin, amin))*(min(a[a.index(amax)+1], b[b.index(bmax)+1])-max(b[b.index(bmin)+1], a[a.index(amin)+1]))
if bmax < amin or amax < bmin:
    s = 0.00
print('{:.2f}'.format(s))
