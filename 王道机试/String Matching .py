t, p = input().strip().split()
nxt = []

def buildnxt():
    nxt.append(0)
    x = 1
    now = 0

    while x < len(p):
        if p[x] == p[now]:
            x += 1
            now += 1
            nxt.append(now)
        elif now:
            now = nxt[now - 1]
        else:
            x += 1
            nxt.append(0)

def find():
    global ans
    tar = 0
    pos = 0
    
    while tar < len(t):
        if t[tar] == p[pos]:
            tar += 1
            pos += 1
        elif pos:
            pos = nxt[pos - 1]
        else:
            tar += 1

        if pos == len(p):
            ans += 1
            pos = nxt[pos - 1]

ans = 0
buildnxt()
find()
print(ans)
