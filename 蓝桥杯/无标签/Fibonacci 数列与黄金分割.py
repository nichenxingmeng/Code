n = int(input().strip())
F1 = 1
F2 = 1
if n <= 100:
    for i in range(2, n+1):
        F1, F2 = F2, F1 + F2
    temp = F1/F2
    print('{:.8f}'.format(temp))
else:
    print(0.61803399)
