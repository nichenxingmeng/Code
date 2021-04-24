n = int(input().strip())

def fanzhuan(n):
    if n == '$':
        return '.'
    else:
        return '$'

def print_(n):
    map = [['$' for _ in range(126)] for _ in range(126)]
    for i in range(2*n):
        if i != 0:
            map[i][i] = fanzhuan(map[i - 1][i - 1])
            map[i][4*n-i] = fanzhuan(map[i - 1][i - 1])
            map[4*n-i][i] = fanzhuan(map[i - 1][i - 1])
            map[4*n-i][4*n-i] = fanzhuan(map[i - 1][i - 1])
        map[i][i+1] = fanzhuan(map[i][i])
        map[i+1][i] = fanzhuan(map[i][i])
        map[i][4*n-i-1] = fanzhuan(map[i][i])
        map[i+1][4*n-i] = fanzhuan(map[i][i])
        map[4*n-i-1][i] = fanzhuan(map[i][i])
        map[4*n-i][i+1] = fanzhuan(map[i][i])
        map[4*n-i-1][4*n-i] = fanzhuan(map[i][i])
        map[4*n-i][4*n-i-1] = fanzhuan(map[i][i])
        for j in range(i+2, 4*n-1-i):
            map[i][j] = map[i][i]
            map[4*n-i][j] = map[i][i]
            map[j][i] = map[i][i]
            map[j][4*n-i] = map[i][i]
    map[0][0] = '.'
    map[0][4*n] = '.'
    map[4*n][0] = '.'
    map[4*n][4*n] = '.'
    map[2*n][2*n] = '$'
    for i in range(4*n+1):
        for j in range(4*n+1):
            print(map[i][j], end='')
        print()

print_(n+1)
