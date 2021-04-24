alist = list(map(int, input().strip().split()))

def quick(alist, l, r):
    i = l
    j = r
    flag = alist[(l + r)//2]
    while i <= j:
        while alist[i] < flag:
            i += 1
        while alist[j] > flag:
            j -= 1
        if i <= j:
            alist[i], alist[j] = alist[j], alist[i]
            i += 1
            j -= 1
    if l < j:
        quick(alist, l, j)
    if i < r:
        quick(alist, i, r)

quick(alist, 0, len(alist)-1)
if alist[0] == 0:
    alist.pop(0)
print(' '.join(map(str, alist)))
