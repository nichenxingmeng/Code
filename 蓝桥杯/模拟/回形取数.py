m, n = map(int, input().split())
t = [[] for x in range(m)]

def pri(t):
    for i in range(len(t)):
        print(t[i][0],end=' ')
    for i in range(1, len(t[0])):
        print(t[len(t)-1][i],end=' ')
    for i in range(len(t)-2,-1,-1):
        print(t[i][len(t[0])-1],end=' ')
    for i in range(len(t[0])-2,0,-1):
        print(t[0][i],end=' ')
    t = t[1:len(t)-1]
    for i in range(len(t)):
        t[i].remove(t[i][0])
        if t[i]:
            t[i].pop()
    return t

if n <= 200 and m <= 200:
    for i in range(m):
        t[i] = list(map(int, input().split()))
    if m == 1:
        for i in range(len(t[0])):
            print(t[0][i],end=' ')
    elif n == 1:
        for i in range(len(t)):
            print(t[i][0],end=' ')
    else:
        while len(t) > 1 and len(t[0]) > 1:
            t = pri(t)
        if t and t != [[]]:
            if len(t) == 1:
                for i in range(len(t[0])):
                    print(int(t[0][i]), end=' ')
            else:
                for i in range(len(t)):
                    print(int(t[i][0]), end=' ')
