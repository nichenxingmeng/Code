n = int(input())
m = list(map(int, input().strip().split()))

def Compactlntegers(m, n):
    for i in range(n):
        if m[i] == 0:
            m[i] = []
    while [] in m:
        m.remove([])
    return len(m)

count = Compactlntegers(m, n)
for i in range(count):
    print(m[i], end=' ')
print('')
print(count)
