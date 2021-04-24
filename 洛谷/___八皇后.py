n = int(input().strip())
a = [0 for _ in range(n+100)]
ans = 0
b1 = [0 for _ in range(n+100)]
b2 = [0 for _ in range(n+100)]
b3 = [0 for _ in range(n+100)]

def dfs(x):
    global ans, b1, b2, b3
    if x > n:
        ans += 1
        for i in range(1, n+1):
            print(a[i], end = '')
        print()
        return
    for i in range(1, n+1):
        if b1[i] == 0 and b2[x+i] == 0 and b3[x-i+15] == 0:
            a[x] = i
            b1[i] = 1
            b2[x+i] = 1
            b3[x-i+15] = 1
            dfs(x+1)
            b1[i] = 0
            b2[x+i] = 0
            b3[x-i+15] = 0

dfs(1)
print(ans)
