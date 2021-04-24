n, m = map(int, input().strip().split())
a = []
for i in range(m):
    a.append([int(j) for j in input().strip().split()])

pingguo = [0 for i in range(n+1)]
for i in range(m):
    pingguo[a[i][0] - 1] += a[i][2]
    pingguo[a[i][1]] -= a[i][2]
for i in range(1, n):
    pingguo[i] += pingguo[i - 1]
pingguo.pop()
print(' '.join(map(str, pingguo)))
