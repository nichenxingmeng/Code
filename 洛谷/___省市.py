mod = 233333
linker = [[0 for _ in range(mod+2)] for _ in range(mod+2)]

def gethash(a, b):
    return (a[0]-'A') + (a[1]-'A')*26 + (b[0]-'A')*26*26 + (b[1]-'A')*26*26*26

def insert(x):
    for i in range(len(linker[x%mod])):
        if linker[x%mod][i][0] == x:
            linker[x%mod][i][1] += 1
            break
    linker[x%mod].append([x, 1])

def find(x):
    for i in range(len(linker[x%mod])):
        if linker[x%mod][i][0] == x:
            return linker[x%mod][i][1]

    return 0

n = int(input().strip())
for i in range(n):
    a, b = map(str, input().strip().split())
    a[2] = 0
    if a[0] != b[0] or a[1] != b[1]:
        ans += find(gethash(b, a))
    insert(gethash(a, b))

print(ans)
