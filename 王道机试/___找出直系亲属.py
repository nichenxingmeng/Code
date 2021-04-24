n, m = map(int, input().strip().split())
fa = [_ for _ in range(27)]
height = [1 for _ in range(27)]

def find(x):
    if fa[x] !=  x:
        fa[x] = find(fa[x])
    return fa[x]

def join(x, y):
    if y == '-':
        return
    f1 = find(x)
    f2 = find(y)
    if f1 != f2:
        if height[f1] > height[f2]:
            fa[f2] = f1
            height[f2] += height[x]
        elif height[f1] < height[f2]:
            fa[f1] =f2
        else:
            fa[f1] = f2
            height[f2] += height[x]

for i in range(n):
    temp = list(input().strip())
    join(ord(temp[0]) - ord('A'), ord(temp[1]) - ord('A'))
    join(ord(temp[0]) - ord('A'), ord(temp[2]) - ord('A'))

print(fa)
print(height)
for i in range(m):
    temp = list(input().strip())
    x, y = ord(temp[0]) - ord('A'), ord(temp[1]) - ord('A')
    if fa[x] != fa[y]:
        print('-')
    else:
        ans = max(height[x], height[y]) - min(height[x], height[y])
        if ans == 1:
            print('parent')
        else:
            ans_ = ans - 2    
            print(ans_)
            print('great_' * ans_, 'grandparent', sep = '')
