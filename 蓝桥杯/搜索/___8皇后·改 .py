b1 = [0 for _ in range(17)]
b2 = [0 for _ in range(17)]
b3 = [0 for _ in range(17)]
max_ = 0
count = 0
qipan = []
for i in range(8):
    qipan.append([int(j) for j in input().strip().split()])

def dfs(x):
    global count, max_
    if x > 8:
        if count > max_:
            max_ = count
        return
    for i in range(1, 9):
        if b1[i] == 0 and b2[x+i] == 0 and b3[x-i+8] == 0:
            b1[i] = 1
            b2[x+i] = 1
            b3[x-i+8] = 1
            count += qipan[x-1][i-1]
            dfs(x+1)
            b1[i] = 0
            b2[x+i] = 0
            b3[x-i+8] = 0
            count -= qipan[x-1][i-1]

dfs(1)
print(max_)
