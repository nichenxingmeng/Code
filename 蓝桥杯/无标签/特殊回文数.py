n = int(input())
for i in range(10000, 1000000):
    if list(str(i)) == list(str(i)[::-1]):
        m = 0
        for j in range(len(list(str(i)))):
            m += int(list(str(i))[j])
        if m == n:
            print(i)
