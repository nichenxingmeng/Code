def go(x, b):
    b[x%10] = 1
    b[x//10%10] = 1
    b[x//100] = 1

def check(x, y, z):
    b = [0 for _ in range(10)]
    if y > 999 or z > 999:
        return False
    go(x, b)
    go(y, b)
    go(z, b)
    for i in range(1, 10):
        if not b[i]:
            return False
    return True

A, B, C = map(int, input().strip().split())

flag = False
for x in range(123, 988):
    if x*B%A or x*C%A:
        continue
    y = x*B//A
    z = x*C//A
    if check(x, y, z):
        print(x, y, z)
        flag = True
if not flag:
    print('No!!!')
