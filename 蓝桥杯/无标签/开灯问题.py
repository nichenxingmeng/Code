n, k = map(int, input().strip().split())
m = [1 for x in range(n)]
for i in range(n):
    for j in range(1, k):
        if (i+1)%(j+1) == 0:
            m[i] = -m[i]

for i in range(len(m)):
    if m[i] == 1:
        print(i+1, end=' ')
