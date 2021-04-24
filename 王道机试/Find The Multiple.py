n = int(input().strip())

Q = []
Q.append(1)

flag = False
cnt = 0
while Q and not flag and cnt <= 100:
    u = Q[0]
    Q.pop(0)
    if u % n == 0:
        print(u)
        cnt += 1
    for i in range(2):
        x = u * 10 + i
        Q.append(x)
