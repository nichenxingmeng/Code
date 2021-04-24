n = int(input().strip())
a1 = []
for i in range(n):
    a1.append(int(input().strip()))
a1.sort()
a1 = [9999 for _ in range(n)]

i, j = 0
sum_ = 0
n2 = 0
for k in range(1, n - 1):
    if a1[i] < a2[j]:
        m = a1[i]
        i += 1
    else:
        m = a2[j]
        j += 1
    if a1[i] < a2[j]:
        m += a1[i]
        i += 1
    else:
        m += a2[j]
        j += 1
    sum_ += m
    a2[n2] = m
    n2 += 1
print(sum_)
