from math import sqrt
n, m = map(int, input().strip().split())
biaoge = []
for i in range(n):
    biaoge.append(input().strip().split())
list = ['A', 'S']

def jisuan():
    global biaoge
    for i in range(n):
        for j in range(m):
            if biaoge[i][j][0] not in list:
                continue
            temp_ = biaoge[i][j]
            temp = []
            for k in range(len(temp_)):
                temp.append(temp_[k])
            a0 = int(''.join(temp[4:temp.index(',')]))
            b0 = int(''.join(temp[temp.index(',')+1:temp.index(':')]))
            temp[temp.index(',')] = '.'
            a1 = int(''.join(temp[temp.index(':')+1:temp.index(',')]))
            b1 = int(''.join(temp[temp.index(',')+1:len(temp)-1]))
            flag = False

            for k in range(a0-1, a1):
                for l in range(b0-1, b1):
                    if biaoge[k][l][0] in list:
                        flag = True
                        break

            if not flag:
                if ''.join(temp[:3]) == 'SUM':
                    ans = 0
                    for k in range(a0-1, a1):
                        for l in range(b0-1, b1):
                            ans += float(biaoge[k][l])
                    biaoge[i][j] = '{:.2f}'.format(ans)
                elif ''.join(temp[:3]) == 'AVG':
                    ans = 0
                    count = 0
                    for k in range(a0-1, a1):
                        for l in range(b0-1, b1):
                            ans += float(biaoge[k][l])
                            count += 1
                    biaoge[i][j] = '{:.2f}'.format(ans/count)
                elif ''.join(temp[:3]) == 'STD':
                    ans = 0
                    count = 0
                    for k in range(a0-1, a1):
                        for l in range(b0-1, b1):
                            ans += float(biaoge[k][l])
                            count += 1
                    pingjunzhi = ans / count
                    ans_ = 0
                    for k in range(a0-1, a1):
                        for l in range(b0-1, b1):
                            ans_ += (float(biaoge[k][l])-pingjunzhi)**2
                    biaoge[i][j] = '{:.2f}'.format(sqrt(ans_/count))
                break

count = 0
for i in range(n):
    for j in range(m):
        if biaoge[i][j][0] not in list:
            count += 1
            biaoge[i][j] = '{:.2f}'.format(float(biaoge[i][j]))
for i in range(n*m - count):
    jisuan()
for i in range(n):
    print(' '.join(biaoge[i]))
