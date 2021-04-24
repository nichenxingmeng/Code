m, n = map(int, input().strip().split())
for i in range(m*2):
    if i % 2 == 0:
        for j in range(n):
            if j != n-1:
                print('+-', end='')
            else:
                print('+-+')
    else:
        for j in range(n):
            if j != n-1:
                print('| ', end='')
            else:
                print('| |')
if m!= 0:
    for j in range(n):
        if j != n-1:
            print('+-', end='')
        else:
            print('+-+')
