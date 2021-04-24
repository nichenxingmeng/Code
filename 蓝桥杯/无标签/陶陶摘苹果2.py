n, m = map(int, input().strip().split())
pingguo = list(map(int, input().strip().split()))

count = 0
for i in range(n):
    if pingguo[i] > m+30:
        count += 1
print(count)
