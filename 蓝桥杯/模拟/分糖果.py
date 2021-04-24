n = int(input().strip())
m = list(map(int, input().strip().split()))

count = 0

while max(m) != min(m):
    for i in range(n):
        m[i] = m[i] // 2
    temp = m[:]
    for i in range(n):
        m[i-1] += temp[i]
    for i in range(n):
        if m[i]&1:
            count += 1
            m[i] += 1
print(count)
