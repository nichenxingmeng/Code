n = str(input().strip())
m = int(input().strip())

def miaoshu(abc):
    global n
    global temp
    nn = []
    count = 0
    if len(n) == 1:
        nn.append('1'+str(n))
        n = ''.join(nn)
        return
    for i in range(len(n)):
        if i == len(n)-1:
            if count == 0:
                nn.append('1'+str(n[i]))
            else:
                nn.append(str(count+1)+str(n[i]))
        elif n[i+1] != n[i] and count == 0:
            nn.append('1'+str(n[i]))
        elif n[i+1] == n[i]:
            count += 1
        else:
            nn.append(str(count+1)+str(n[i]))
            count = 0
    n = ''.join(nn)

count0 = 0
while count0 < m:
    miaoshu(n)
    count0 += 1
for x in n:
    print(x, end='')
    
