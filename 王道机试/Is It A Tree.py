n = int(input().strip())
visit = [False for _ in range(2 * n + 1)]
father = [i for _ in range(2 * n + 1)]
height = [0 for _ in range(2 * n + 1)]
InDegree = [0 for _ in range(2 * n + 1)]

def find(x):
    if father[x] != x:
        father[x] = find(father[x])
    return father[x]

def join(x, y):
    x1 = find(x)
    y1 = find(y)
    if x1 != y1:
        if height[x1] < height[y1]:
            father[x1] = y1
        elif height[x1] > height[y1]:
            father[y1] = x1
        else:
            father[y1] = x1
            height[x1] += 1

def IsTree():
    component = 0
    root = 0
    flag = True

    for i in range(1, 2 * n + 1):
        if not visit[i]:
            continue
        if father[i] == i:
            component += 1
        if component > 1:
            flag = False
            break
        if InDegree[i] == 0:
            root += 1
        if root > 1:
            flag = False
            break

    if (component == 0 and root != 0) or (component != 0 and root == 0):
        flag = False
    return flag
            
for i in range(n):
    x, y = map(int, input().strip().split())
    join(x, y)
    InDegree[y] += 1
    visit[x] = True
    visit[y] = True

if IsTree():
    print('YES')
else:
    print('NO')
