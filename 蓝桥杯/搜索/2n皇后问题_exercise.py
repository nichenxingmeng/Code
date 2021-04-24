n = int(input())
m = []
a = [[] for x in range(n)]

for i in range(n):
    m.append(list(map(int,input().split())))
    
t = m[:]

for i in range(n):
    for j in range(n):
        t[i] = m[i][:]
        if t[i][j] == 1:
            t[i][j] = 2
        a[i].append(t[i])
#print(a)

o = []
i = [[] for x in range(n)]

def possible(n, c):
    global o
    global a
    global i
    if c == n-1:
        for j in range(0, n):
            i[c] = j
            t = []
            x = 0
            while x < n:
                t += [a[x][i[x]]]
                x += 1
            o.append(t)
        c = 0
    else:
        for j in range(0, n):
            i[c] = j
            possible(n, c+1)

possible(n, 0)

for i in range(len(o)):
    flag = True
    for k in range(n):
        for j in range(n):
            for l in range(n):
                if o[i][j][k]== 2 and o[i][l][k] == 2 and j != l:
                    flag = False
    if not flag:
        o[i] = []

while [] in o:
    o.remove([])

#print(o,len(o))

ab = [[[] for x in range(n)] for x in range(len(o))]
f = [[[] for x in range(n)] for x in range(len(o))]
for i in range(len(o)):
    for j in range(n):
        for k in range(n):
            ab[i][j] = o[i][j][:]
            if ab[i][j][k] == 1:
                ab[i][j][k] = 3
                f[i][j].append(ab[i][j])

#print(f,len(f))

for x in f:
    if len(x) < n:
        f.remove(x)
for i in range(len(f)):
    for j in range(n):
        if len(f[i][j]) < n-1:
            f[i][j].append([])
#print(f,len(f))

q = []
for i in range(0, (n-1)**n):
    q.append(bin(i)[2:])
    while len(q[i]) < n:
        q[i] = '0'+q[i]

g = []
for i in range(len(f)):
    t = 0
    while t < len(q):
        h = []
        for j in range(n):
            h += [f[i][j][int(q[t][j])]]
        t += 1
        g.append(h)

#print(g, len(g))

while i < len(g):
    for j in range(n):
        if g[i][j] == []:
            g.remove(g[i])
            i -= 1
    i += 1

#print(g, len(g))

for i in range(len(g)):
    flag = True
    for k in range(n):
        for j in range(n):
            #print(i,j,k)
            if g[i][j] != []:
                if g[i][j][k] == 3:
                    for l in range(n):
                        if g[i][l] != []:
                            if g[i][l][k] == g[i][j][k] and j != l:
                                flag = False
    if not flag:
        g[i] = []

while [] in g:
    g.remove([])

i = 0
while i < len(g):
    if [] in g[i]:
        g.remove(g[i])
        i -= 1
    i += 1

i = 0
while i < len(g):
    flag = True
    for j in range(n):
        if i < len(g):
            if 2 not in g[i][j] or 3 not in g[i][j]:
                g.remove(g[i])
                flag = False
    if not flag:
        i -= 1
    i += 1

print(g, len(g))
