n = int(input().strip())
m = list(map(int, input().strip().split()))

ans = 0
max_ = max(m)
for i in range(n):
    a = m[i]
    for j in range(i + 1, n - 1):
        if m[j] == max_:
            continue
        if m[j] > a:
            b = m[j]
            for k in range(j + 1, n):
                if m[k] > b:
                    ans += 1
print(ans)
