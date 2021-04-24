n, s = map(int, input().strip().split())

for i in range(10000):
    count = i
    count_ = i
    for j in range(n):
        count += 2*(count_)-1
        count_ = 2*(count_)-1
    if count == s:
        print(i)
        break
