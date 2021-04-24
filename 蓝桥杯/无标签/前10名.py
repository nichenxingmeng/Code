n = int(input())
m = list(map(int, input().strip().split()))
m.sort(reverse = True)
for i in range(10):
    print(m[i], end=' ')
