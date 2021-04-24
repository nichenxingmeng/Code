n = int(input().strip())
louceng = [0 for i in range(n+1)]
for i in range(1, n+1):
    louceng[i] = int(input().strip())
Q = []
louceng_ = [0 for i in range(n+1)]
a, b = map(int, input().strip().split())
louceng_[a] = 1
Q.append([a, 0])

while Q:
    temp = Q[0]
    Q.pop(0)
    temp0 = temp[0]
    temp1 = temp[1]
    if temp0 == b:
        break
    for i in range(-1, 2, 2):
        te0 = temp0 + i*louceng[i]
        temp1 += 1
        if te0 < 1 or te0 > n or louceng_[te0] != 0:
            continue
        Q.append([te0, temp1])
        louceng_[te0] = 1

if temp0 == b:
    print('find')
else:
    print(-1)
        
        

