'''
from math import sqrt

def prime(x):
    for i in range(2, int(sqrt(x))+1):
        if x % i == 0:
            return False
    return True

def count1(x):
    x = bin(x)[2:]
    return x.count('1')

n, k = map(int, input().strip().split())
a = list(map(int, input().strip().split()))

U = 1 << n
ans = 0
for i in range(U):
    if count1(i) == k:
        sum_ = 0
        for j in range(n):
            if x & (1 << j):
                sum_ += a[j]
        if prime(sum_):
            ans += 1
print(ans)
'''
'''
n, r = map(int, input().strip().split())
a = [0 for _ in range(n)]

for S in range((1<<n)-1, -1, -1):
    cnt = 0
    for i in range(n):
        if S & (1<<i):
            a[cnt] = i
            cnt += 1
    if cnt == r:
        for i in range(r-1, -1, -1):
            print(n - a[i], end = '')
        print()
'''
'''
n, r = map(int, input().strip().split())
a = [0 for _ in range(n)]

for S in range((1<<n)-1, -1, -1):
    cnt = 0
    for i in range(n):
        if S & (1<<i):
            a[cnt] = i
            cnt += 1
    if cnt == r:
        for i in range(r-1, -1, -1):
            print(n - a[i], end = '')
        print()
'''
