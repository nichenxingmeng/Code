'''
n = int(input().strip())
k = int(input().strip())

def njinzhi(first, n):
    temp = []
    while first >= n:
        temp.append(str(first%n))
        first = first//n
    temp.append(str(first))
    return ''.join(temp[::-1])

count = k**n-k**(n-1)
for i in range(k**(n-1), k**n):
    temp = njinzhi(i, k)
    if '00' in temp:
        count -= 1
print(count)
'''
n = int(input().strip())
k = int(input().strip())

def c(m, n):
    s = 1
    for i in range(n):
        s *= m - i
    for i in range(1, n+1):
        s //= i
    return s

ans = 0
for i in range(n // 2 + 1):
    ans += (k-1) ** (n-i) * c(n-i,i)

print(ans)
