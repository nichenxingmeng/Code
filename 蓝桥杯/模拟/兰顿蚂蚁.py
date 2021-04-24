m, n = map(int, input().strip().split())
ditu = []
for i in range(m):
    ditu.append(list(map(int, input().strip().split())))
a, b, c, d = map(str, input().strip().split())
start = [int(a), int(b), c]
count = int(d)

def youzhuan(d):
    if d == 'U':
        return 'R'
    if d == 'D':
        return 'L'
    if d == 'L':
        return 'U'
    if d == 'R':
        return 'D'
def zuozhuan(d):
    if d == 'U':
        return 'L'
    if d == 'D':
        return 'R'
    if d == 'L':
        return 'D'
    if d == 'R':
        return 'U'
def qianjin(d):
    global start
    if d == 'U':
        start[0] -= 1
    if d == 'D':
        start[0] += 1
    if d == 'L':
        start[1] -= 1
    if d == 'R':
        start[1] += 1 

while count > 0:
    if ditu[start[0]][start[1]] == 0:
        start[2] = zuozhuan(start[2])
        ditu[start[0]][start[1]] = 1
        qianjin(start[2])
    else:
        start[2] = youzhuan(start[2])
        ditu[start[0]][start[1]] = 0
        qianjin(start[2])
    count -= 1
print(start[0], start[1], sep=' ')
