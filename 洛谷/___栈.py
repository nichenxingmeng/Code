h = [1 for _ in range(19)]
n = int(input().strip())

for i in range(2, n+1):
    for j in range(i):
        h[i] += h[j]*h[i-j-1]

print(h[n])

n = int (input().strip())
h = [1 for _ in range(n + 1)]

for i in range(2, n + 1):
    for j in range(i):
        h[i] = h[j] * h[i - j - 1]

print(h[n])
