from math import sqrt

n = int(input().strip())

MAX = int(sqrt(n + 1))

zhishu = [True if i & 1 else False for i in range(MAX + 1)]
zhishu[0], zhishu[1], zhishu[2] = False, False, True
for i in range(2, int(sqrt(MAX)) + 1):
    j = i
    if zhishu[i]:
        while i * j <= MAX:
            zhishu[i * j] = False
            j += 1

ans = 0
for i in range(2, MAX):
    if n == 1:
        break
    if zhishu[i]:
        tmp = i
        while n % tmp == 0:
            ans += 1
            n = n // i

if n != 1:
    ans += 1

print(ans)
