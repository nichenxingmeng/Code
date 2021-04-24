from copy import deepcopy
t = int(input().strip())
m = [[0,[],0,[]] for _ in range(t)]
for i in range(t):
    m[i][0] = int(input().strip())
    for j in range(m[i][0]):
        m[i][1].append(list(input().strip()))
    m[i][2] = int(input().strip())
    for j in range(m[i][2]):
        m[i][3].append(list(input().strip()))

def caozuo(m):
    migong = deepcopy(m[1])
    for j in range(m[0]):
        for k in range(m[0]):
            if migong[j][k] == 'S':
                start = [j, k]
                temp = deepcopy(start)
    mingling = deepcopy(m[3])
    for j in range(len(mingling)):
        flag = True
        start = deepcopy(temp)
        for k in range(len(mingling[j])):
            if mingling[j][k] == 'L':
                start[1] -= 1
            elif mingling[j][k] == 'R':
                start[1] += 1
            elif mingling[j][k] == 'U':
                start[0] -= 1
            else:
                start[0] += 1
            if start[0] < 0 or start[0] >= m[0] or start[1] < 0 or start[1] >= m[0]:
                print('I am out!')
                flag = False
                break
            if migong[start[0]][start[1]] == '#':
                print('I am dizzy!')
                flag = False
                break
            if migong[start[0]][start[1]] == 'T':
                print('I get there!')
                flag = False
                break
        if flag:
            print('I have no idea!')

for i in range(t):
    caozuo(m[i])
