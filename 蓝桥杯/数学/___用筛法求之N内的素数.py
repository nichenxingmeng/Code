from math import sqrt
n = int(input().strip())
m = [True if i&1 else False for i in range(n+1)]
m[0], m[1], m[2] = False, False, True
for i in range(2, int(sqrt(len(m)))+1):
    j = i
    if m[i]:
        while j*i <= n:
            m[j*i] = False
            j += 1
for i in range(2, n+1):
    if m[i]:
        print(i)
