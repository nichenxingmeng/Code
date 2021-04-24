n = int(input())
m = [[] for x in range(n+1)]

def Cnk(n, k, i):
    global count
    if i == k:
        count *= (n-k+1)/k
    else:
        count *= (n+1-i)/i
        Cnk(n, k, i+1)


for x in range(1, n+1):
    for y in range(1,x):
        count = 1
        Cnk(x, y, 1)
        count += 0.5
        temp = int(count)
        m[x].append(temp)

m[0] = [1]
m[1] = [1,1]
for i in range(2, len(m)):
    m[i].insert(0, 1)
    m[i].append(1)

for i in range(len(m)-1):
    print(' '*((len(m)-i-1)*3+2), end='')
    for j in range(len(m[i])):
        if j > 0:
            print(' '*(6-len(str(m[i][j]))), end='')
        print(m[i][j], end='')
    print('')
    
i = len(m)-1
print(' '*((len(m)-i-1)*3+2), end='')
for j in range(len(m[i])):
    if j > 0:
        print(' '*(6-len(str(m[i][j]))), end='')    
    print(m[i][j], end='')
