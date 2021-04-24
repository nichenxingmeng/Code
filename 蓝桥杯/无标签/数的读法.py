p = []
m = []
n = list(str(input().strip()))
d = {'1':'yi', '2':'er','3':'san','4':'si','5':'wu','6':'liu','7':'qi','8':'ba','9':'jiu','0':'ling'}
cout = 0
while len(n) > 4:
    m.insert(0, n[-4:])
    n.pop()
    n.pop()   
    n.pop()
    n.pop()
m.insert(0,n[:])
for i in range(len(m)):
    for j in range(len(m[i])):
        if m[i][j] == '0': 
            p.append(d[m[i][j]])
        else:
            p.append(d[m[i][j]])
            if len(m[i]) == 4:
                if j == 0:
                    p.append('qian')
                elif j == 1:
                    p.append('bai')
                elif j == 2:
                    p.append('shi')
            if len(m[i]) == 3:
                if j == 0:
                    p.append('bai')
                elif j == 1:
                    p.append('shi')
            if len(m[i]) == 2:
                if j == 0:
                    p.append('shi')
    if m[i][-1] == 'ling':
        m[i][-1] = ' '
    if len(m) == 3:
        if i == 0:
            p.append('yi')
        if i == 1:
            p.append('wan')
    if len(m) == 2:
        if i == 0:
            p.append('wan')
if p[0] == 'yi' and p[1] != 'yi' and p[1] != 'wan':
    p.remove(p[0])
count = 0
for i in range(len(p)):
    if p[i] == 'ling':
        count += 1
        if count > 1:
            p[i] = ' '
    else:
        count = 0
while p[-1] == ' ':
      p.remove(p[-1])
while p[-1] == 'ling':
    p.remove(p[-1])
if p[-1] == 'wan' and p[-2] == 'yi' and len(p) > 2:
    p.remove(p[-1])
while ' ' in p:
    p.remove(' ')
for i in range(len(p)-1):
    print(p[i], end=' ')
print(p[-1], end='')


