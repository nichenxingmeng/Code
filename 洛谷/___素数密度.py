from math import sqrt

def shaixuan(n):
    global nums
    nums = [True if i & 1 else False for _ in range(n + 1)]
    nums[0], nums[1], nums[2] = False, False, True
    for i in range(2, int(sqrt(n)) + 1):
        j = i
        if nums[i]:
            while j * i <= n:
                nums[j * i] = False
                j += 1
    return

nums = []
shaixuan(50000)

L, R = map(int, input().strip().split())
a = []
for i in range(L, R + 1):
    a.sppend(i)

for i in range(2, int(sqrt(R)) + 1):
    j = i
    if nums[i]:
        while i * j <= R:
            if i * j >= L:
                a[j * i - L] = 0
            j += 1

ans = 0
for i in range(R - L + 1):
    if a[i] != 0:
        ans += 1
print(ans)
