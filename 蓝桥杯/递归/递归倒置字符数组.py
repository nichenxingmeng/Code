shuru = input().strip().split()
n = shuru[0]
s = shuru[1]

count = 0
def daozhi(n):
    global count
    global s
    if count <= n // 2 - 1:
        s = list(s)
        s[count], s[n-1-count] = s[n-1-count], s[count]
        s = ''.join(s)
        count += 1
        print(s)
        daozhi(n)
    else:
        return
daozhi(int(n))
print()
print(s)

