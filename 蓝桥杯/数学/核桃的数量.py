a, b, c = map(int, input().strip().split())
for i in range(max(a, b, c), 25000):
    if i % a == 0 and i % b == 0 and i % c == 0:
        print(i)
        break
